#!C:\Users\mikae\AppData\Local\Programs\Python\Python36-32\python.exe
"""
A CGI-script for python, including error handling.

Change the shebang to your path to the python executable.
"""

try:
    from wsgiref.handlers import CGIHandler
    from app import app

    CGIHandler().run(app)

except Exception as e: #pylint: disable=broad-except
    import traceback

    print("Content-Type: text/plain;charset=utf-8")
    print("")
    print(traceback.format_exc())
