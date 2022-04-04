#!/usr/bin/env python
#encoding:utf-8

import datetime

from typing import Optional

from . import ItemBase



class PhotoCreateSchema(ItemBase):

    pic_time: datetime.datetime
    title : str
    description: Optional[str] = None
    upload_user_id: int
    upload_file: str