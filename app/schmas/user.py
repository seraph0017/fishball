#!/usr/bin/env python
#encoding:utf-8

from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    is_active: bool = True
    is_superuser: bool = False
    user_type: int
    nick_name: str
    hashed_password: str
    photo_url: str


class UserCreate(BaseModel):
    email: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    user_type: int
    nick_name: str
    hashed_password: str
    photo_url: str


class UserUpdate(BaseModel):
    email: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    user_type: int
    nick_name: str
    hashed_password: str
    photo_url: str



class UserLogin(BaseModel):
    username: str
    password: str