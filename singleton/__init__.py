# -*- coding: utf-8 -*-

try:
    from .singleton import singleton
    print("use python3")
except ImportError:
    from singleton import singleton
    print("use python2")
