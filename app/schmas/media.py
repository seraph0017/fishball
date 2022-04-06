#!/usr/bin/env python
#encoding:utf-8

import datetime

from typing import Optional

from . import ItemBase




class MediaEditSchema(ItemBase):

    mediaTitle: str
    mediaDescription: str
    mediaTime: datetime.date