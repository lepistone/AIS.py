# -*- coding: utf-8 -*-
"""
AIS.py - A Python interface for the Swisscom All-in Signing Service.

:copyright: (c) 2016 by Camptocamp
:license: AGPLv3, see README and LICENSE for more details

"""
from .api import login
from .ais import AIS, Signature
from .exceptions import AISError, AuthenticationFailed

__all__ = ('login', 'AIS', 'Signature', 'AISError', 'AuthenticationFailed')

__version__ = '0.1.0a1'
