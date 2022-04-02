#!/usr/biu/env python
# encoding:utf-8

from os import path

STATIC_FILES_PATH = path.join(path.abspath("."), "app", "statics")
TEMPLATE_FILES_PATH = path.join(path.abspath("."), "app", "templates")
UPLOADS_FILES_PATH = ""
DATABASE_URI = ""


try:
    from local_configs import *
except Exception as e:
    pass
