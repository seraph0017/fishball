#!/usr/biu/env python
# encoding:utf-8


from sqlalchemy import Column, String, Boolean, Integer
from . import Base


class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    user_name = Column(String(length=1024))
    nick_name = Column(String(length=1024))
    photo_url = Column(String(length=1024))
