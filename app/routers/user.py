#!/usr/bin/env python
#encoding:utf-8

import configs

from fastapi import APIRouter, Request, UploadFile, Form



user_router = APIRouter(prefix="/user", tags=["user"])