#!/usr/bin/env python
# encoding:utf-8

import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from . import Base

column_default_text = "这个人很懒，什么都没有写"


class Photo(Base):
    __tablename__ = "photos"

    is_active = Column(Boolean, default=True)
    pic_time = Column(DateTime, default=datetime.datetime.now())
    title = Column(String, default=column_default_text)
    description = Column(Text, default=column_default_text)
    upload_user_id = Column(Integer)
    pic_year = Column(Integer)
    pic_month = Column(Integer)

    id = Column(Integer, primary_key=True, index=True)
    update_time = Column(DateTime, onupdate=datetime.datetime.now())
    create_time = Column(DateTime, default=datetime.datetime.now())
    is_active = Column(Boolean, default=True)


PydanticPhoto = sqlalchemy_to_pydantic(Photo)
