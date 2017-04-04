# pysingleton
> module which provides a decorator to create thread-safe singleton classes <br />
> *Version: 0.2.1*

## ABANDONED!!!

Please, don't use this anymore ..

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
from singleton import singleton

@singleton()
class MySingleton(object):
    pass

o = MySingleton()
o2 = MySingleton()

print o is o2
```
