#!/usr/bin/env python
#encoding:utf-8

from app.service.user import create_user
import configs

from fastapi import APIRouter, Request, UploadFile, Form
from starlette.responses import RedirectResponse
from app.schmas.user import UserCreate



user_router = APIRouter(prefix="/users", tags=["user"])




@user_router.post("/", name="user_add")
def user_add_handle(request: Request, userCreate: UserCreate):
    if request.state.user:
        create_user(userCreate)
        return "ok"
    return RedirectResponse(url=configs.LOGIN_PAGE)