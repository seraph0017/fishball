#!/usr/bin/env python
# encoding:utf-8

import datetime


from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text, Date
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from . import Base

column_default_text = "这个人很懒，什么都没有写"


class Medias(Base):

    __tablename__ = "medias"

    title = Column(String, default=column_default_text)
    description = Column(Text, default=column_default_text)
    pic_time = Column(Date, default=datetime.date.today)

    upload_local_file_path = Column(String)
    upload_oss_file_path = Column(String)
    upload_cdn_file_path = Column(String)
    upload_render_file_path = Column(String)
    upload_user_id = Column(Integer)
    pic_year = Column(Integer)
    pic_month = Column(Integer)
    is_pic = Column(Boolean)

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    update_time = Column(DateTime, onupdate=datetime.datetime.now, default=datetime.datetime.now)
    create_time = Column(DateTime, default=datetime.datetime.now)
    is_active = Column(Boolean, default=True)










