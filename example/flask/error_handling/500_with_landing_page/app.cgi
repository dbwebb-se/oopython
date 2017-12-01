#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Smallest possible cgi-script to execute a WSGI application like Flask.
"""

from wsgiref.handlers import CGIHandler
from app import app

CGIHandler().run(app)
