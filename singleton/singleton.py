# -*- coding: utf-8 -*-

import thread


def Singleton(decorated_class):
    """decorator for a thread-safe singleton pattern.
        Please just use the singleton pattern if it is not
        possible do solve your problem in another way.

        Example:

        >>> @Singleton
        ... class MySingleton(object):
        ...     pass
        >>> o = MySingleton()
        >>> o2 = MySingleton()
        >>> print o is o2

    """
    class _Singleton(decorated_class):
        _instance = None
        _lock = thread.allocate_lock()

        def __new__(cls, *args, **kwargs):
            with cls._lock:
                if _Singleton._instance is None:
                    _Singleton._instance = super(_Singleton, cls).__new__(cls, *args, **kwargs)
                    _Singleton._instance._initialized = False
            return _Singleton._instance

        def __init__(self, *args, **kwargs):
            if self._initialized:
                return
            super(_Singleton, self).__init__(*args, **kwargs)
            self._initialized = True

    _Singleton.__name__ = decorated_class.__name__
    return _Singleton
