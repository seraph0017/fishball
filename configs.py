#!/usr/biu/env python
# encoding:utf-8

import datetime
from os import path

STATIC_FILES_PATH = path.join(path.abspath("."), "app", "statics")
TEMPLATE_FILES_PATH = path.join(path.abspath("."), "app", "templates")
UPLOADS_FILES_PATH = ""
DATABASE_URI = ""
REDIS_URI = ""
DEPLOY_ENV_URI = ""

LOGFILE_PATH = path.join(path.abspath("."), "log")


F_BIRTHDAY = datetime.date(1988, 9, 8)
C_BIRTHDAY = datetime.date(2020, 7, 3)

ONE_PAGE_LIMIT = 12


SECRET = ""
LOGIN_PAGE = ""


try:
    from local_configs import *
except Exception as e:
    pass
