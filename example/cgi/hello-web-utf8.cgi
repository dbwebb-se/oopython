#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Execute as cgi-skript and send a correct HTTP header.
Works with UTF-8 characters.

"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


# Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()



# Send the HTTP header for plain text or for html
#print("Content-Type: text/plain;charset=utf-8")
print("Content-Type: text/html;charset=utf-8")
print("")


# Here comes the content of the webpage 
content = """
<h1>Hello The World of Web</h1>
<p>Ohhh! CGI works!
"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
