#!/usr/bin/env python
from wsgiref.simple_server import make_server
from search import application
httpd=make_server('',8000,application)
print('start');
httpd.serve_forever();
