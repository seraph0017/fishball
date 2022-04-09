#!/usr/biu/env python
# encoding:utf-8


from enum import Enum
from email.policy import default
from fastapi import Request
from sqlalchemy import Column, String, Boolean, Integer
from sqladmin import ModelAdmin
from . import Base
from devtools import debug


class UserType(Enum):

    ADMIN = 0
    FAMILY = 1
    FRIEND = 2
    OTHER = 3


class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    user_type = Column(Integer, default=UserType.FRIEND)
    nick_name = Column(String(length=1024))
    photo_url = Column(String(length=1024))


