#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pylint: disable=import-outside-toplevel

"""
A CGI-script for python, including error handling.
"""

try:
    from wsgiref.handlers import CGIHandler
    from app import app

    CGIHandler().run(app)

except Exception as e:
    import traceback

    print("Content-Type: text/plain;charset=utf-8")
    print("")
    print(traceback.format_exc())