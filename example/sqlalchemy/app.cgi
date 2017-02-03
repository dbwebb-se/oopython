#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

""" cgi-script to execute a WSGI application """

from wsgiref.handlers import CGIHandler
from app import app

CGIHandler().run(app)
