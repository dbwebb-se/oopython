#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
A CGI-script for python, including error handling.
"""

try:
    #pylint: disable=import-outside-toplevel
    from wsgiref.handlers import CGIHandler
    from app import app

    CGIHandler().run(app)

except Exception as e:
    #pylint: disable=import-outside-toplevel
    import traceback

    print("Content-Type: text/plain;charset=utf-8")
    print("")
    print(traceback.format_exc())