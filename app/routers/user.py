#!/usr/bin/env python
# encoding:utf-8

from app.service.user import create_user, update_user_by_id
import configs

from fastapi import APIRouter, Request, UploadFile, Form
from starlette.responses import RedirectResponse
from app.schmas.user import UserCreate, UserUpdate


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
