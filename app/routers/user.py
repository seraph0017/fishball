#!/usr/bin/env python
# encoding:utf-8

from app.service.user import change_password_by_id, create_user, update_user_by_id
import configs

from fastapi import APIRouter, Request, UploadFile, Form
from starlette.responses import RedirectResponse
from app.schmas.user import ChangePWD, UserCreate, UserUpdate


user_router = APIRouter(prefix="/users", tags=["user"])


@user_router.post("/", name="user_add")
def user_add_handle(request: Request, userCreate: UserCreate):
    if request.state.user:
        create_user(userCreate)
        return "ok"
    return RedirectResponse(url=configs.LOGIN_PAGE)


@user_router.patch("/{user_id}", name="user_update")
def user_update_handle(request: Request, user_id: int, userUpdate: UserUpdate):
    if request.state.user:
        update_user_by_id(user_id, userUpdate)
        return "ok"
    return RedirectResponse(url=configs.LOGIN_PAGE)


@user_router.post("/changepwd/{user_id}", name="change_pwd")
def change_pwd_handle(request: Request, user_id: int, changePWD: ChangePWD):
    if request.state.user:
        u = change_password_by_id(user_id, changePWD)
        return u
    return RedirectResponse(url=configs.LOGIN_PAGE)
