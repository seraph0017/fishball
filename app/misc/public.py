#!/usr/bin/env python
#encoding:utf-8
import configs
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory=configs.TEMPLATE_FILES_PATH)