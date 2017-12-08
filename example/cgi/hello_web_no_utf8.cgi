#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Test for CGI program which uses no UTF-8 characters, including error handling.
"""

try:
    # Enable debugging
    import cgitb
    cgitb.enable()

    # Write out the HTTP header
    print("Content-Type: text/html;charset=utf-8")
    print("")

    # Write out the page content
    print("<h1>Hello World!</h1>")
    print("<p>Ohhh! CGI works!")

except Exception as e: #pylint: disable=broad-except
    import traceback

    print("Content-Type: text/plain;charset=utf-8")
    print("")
    print(traceback.format_exc())
