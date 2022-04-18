#!/usr/bin/env python
# encoding:utf-8

import datetime

from typing import Optional


from . import ItemBase


class MediaEditSchema(ItemBase):

    mediaTitle: str
    mediaDescription: str
    mediaTime: datetime.date
    is_active: Optional[bool] = True 
    group_id: Optional[int] = 1


class MediaGroupCreateSchema(ItemBase):

    title: str
    description: Optional[str] = None
    group_level: Optional[int]


class MediaGroupUpdateSchema(ItemBase):

    title: str
    description: Optional[str] = None
    group_level: Optional[int]
    is_active: Optional[bool] = True
