#!C:\Users\mikae\AppData\Local\Programs\Python\Python36-32\python.exe
"""
Smallest possible cgi-script to execute a WSGI application like Flask.

Change the shebang to your path to the python executable.
"""

from wsgiref.handlers import CGIHandler
from app import app

CGIHandler().run(app)
