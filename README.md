# pysingleton
> module which provides a decorator to create thread-safe singleton classes <br />
> *Version: 0.00.01*

***

**Author:** Timo Furrer <tuxtimo@gmail.com><br />
**Version:** 0.00.01 <br />

## I know

I know that singletons are **evil**!

## How to install

Install it with:

    $ sudo python setup.py install

## Use

Use it in your python programs with:

```python
from singleton import Singleton

@Singleton
class MySingleton(object):
    pass

o = MySingleton()
o2 = MySingleton()

print o is o2
```
