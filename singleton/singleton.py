# -*- coding: utf-8 -*-

import thread


def singleton(multi_init=False):
    def _singleton_decorator(decorated_class):
        """decorator for a thread-safe singleton pattern.
            Please just use the singleton pattern if it is not
            possible do solve your problem in another way.

            Example:

            >>> @singleton()
            ... class MySingleton(object):
            ...     pass
            >>> o = MySingleton()
            >>> o2 = MySingleton()
            >>> print o is o2

        """
        class _singleton(decorated_class):
            _instance = None
            _lock = thread.allocate_lock()

            def __new__(cls, *args, **kwargs):
                with cls._lock:
                    if _singleton._instance is None:
                        _singleton._instance = super(_singleton, cls).__new__(cls, *args, **kwargs)
                        _singleton._instance._initialized = False
                return _singleton._instance

            def __init__(self, *args, **kwargs):
                if self._initialized and not multi_init:
                    return
                super(_singleton, self).__init__(*args, **kwargs)
                self._initialized = True

        _singleton.__name__ = decorated_class.__name__
        return _singleton
    return _singleton_decorator
