#!/usr/bin/env python
# encoding:utf-8

from app.service.media import (
    get_all_media_group,
    get_media_count,
    get_media_group_count,
)
from app.service.user import get_all_user, get_user_by_id, get_user_count
import configs
from fastapi import APIRouter, Request
from app.misc.public import templates
from starlette.responses import RedirectResponse


admin_router = APIRouter(prefix="/admin", tags=["admin"])


@admin_router.get("/", name="admin_dashboard")
def admin_handle(request: Request):
    if request.state.user and request.state.user.is_superuser:
        user_count = get_user_count()
        media_count = get_media_count()
        media_group_count = get_media_group_count()
        re_context = dict(
            request=request,
            title="鱼丸札记",
            user_count=user_count,
            media_count=media_count,
            media_group_count=media_group_count,
        )
        return templates.TemplateResponse("admin/admin_base.jinja2", re_context)
    return RedirectResponse(url=configs.LOGIN_PAGE)


@admin_router.get("/user", name="admin_user_list")
def admin_user_handle(request: Request):
    if request.state.user and request.state.user.is_superuser:
        user_list = get_all_user()
        re_context = dict(
            request=request,
            title="鱼丸札记",
            user_list=user_list,
        )
        return templates.TemplateResponse("admin/admin_user.jinja2", re_context)
    return RedirectResponse(url=configs.LOGIN_PAGE)


@admin_router.get("/user/{user_id}", name="admin_user_detail")
def admin_user_detail_handle(request: Request, user_id: int):
    if request.state.user and request.state.user.is_superuser:
        user = get_user_by_id(user_id)
        re_context = dict(
            request=request,
            title="鱼丸札记",
            user=user,
        )
        return templates.TemplateResponse("admin/admin_user_detail.jinja2", re_context)
    return RedirectResponse(url=configs.LOGIN_PAGE)


@admin_router.get("/media", name="admin_media_list")
def admin_media_handle():
    pass


@admin_router.get("/media/{media_id}", name="admin_media_detail")
def admin_media_detail_handle(media_id):
    pass


@admin_router.get("/mediagroup", name="admin_media_group_list")
def admin_media_group_handle(request: Request):
    if request.state.user and request.state.user.is_superuser:
        media_group_list = get_all_media_group()
        re_context = dict(
            request=request,
            title="鱼丸札记",
            media_group_list=media_group_list,
        )
        return templates.TemplateResponse("admin/admin_mediagroup.jinja2", re_context)
    return RedirectResponse(url=configs.LOGIN_PAGE)


@admin_router.get("/mediagroup/{media_group_id}", name="admin_media_group_detail")
def admin_media_detail_handle(media_group_id):
    pass
