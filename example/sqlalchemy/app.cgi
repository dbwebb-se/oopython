#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
A CGI-script for python, including error handling.
"""

try:
    from app import app
    from wsgiref.handlers import CGIHandler

    CGIHandler().run(app)

except Exception as e:
    import traceback

    print("Content-Type: text/plain;charset=utf-8")
    print("")
    print(traceback.format_exc())
