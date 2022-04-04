#!/usr/bin/env python
#encoding:utf-8

import sys
import configs

from os import path

from loguru import logger

logger.add(path.join(configs.LOGFILE_PATH, 'info.log'), rotation="1 week", level="INFO") 
logger.add(path.join(configs.LOGFILE_PATH, 'debug.log'), rotation="1 week", level="DEBUG") 

