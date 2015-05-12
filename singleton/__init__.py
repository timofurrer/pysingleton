# -*- coding: utf-8 -*-

try:
    from .singleton import singleton
except ImportError:
    from singleton import singleton
