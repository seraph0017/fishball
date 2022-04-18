#!/usr/bin/env python
# encoding:utf-8

from app.service.media import (
    convert_page_to_skip_limit,
    get_all_media_group,
    get_all_medias,
    get_all_page_num,
    get_media_by_id,
    get_media_count,
    get_media_group_by_id,
    get_media_group_count,
    get_medias,
    get_page_num_list,
)
from app.service.user import get_all_user, get_user_by_id, get_user_count
from app.sqls import media
import configs
from fastapi import APIRouter, Request
from app.misc.public import templates
from starlette.responses import RedirectResponse
from devtools import debug


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
def admin_media_handle(request: Request, page_num: int = 1):
    if request.state.user and request.state.user.is_superuser:
        skip, limit = convert_page_to_skip_limit(page_num)
        media_list = get_all_medias(skip, limit)
        all_page_num = get_all_page_num()
        page_num_list = get_page_num_list(all_page_num, page_num)
        re_context = dict(
            request=request,
            title="鱼丸札记",
            media_list=media_list,
            total_page_num=all_page_num,
            now_page_num=page_num,
            page_num_list = page_num_list,
        )
        return templates.TemplateResponse("admin/admin_media.jinja2", re_context)
    return RedirectResponse(url=configs.LOGIN_PAGE)


@admin_router.get("/media/{media_id}", name="admin_media_detail")
def admin_media_detail_handle(request: Request, media_id: int):
    if request.state.user and request.state.user.is_superuser:
        media = get_media_by_id(media_id)
        re_context = dict(
            request=request,
            title="鱼丸札记",
            media=media,
        )
        return templates.TemplateResponse(
            "admin/admin_media_detail.jinja2", re_context
        )
    return RedirectResponse(url=configs.LOGIN_PAGE)


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
def admin_media_detail_handle(request: Request, media_group_id: int):
    if request.state.user and request.state.user.is_superuser:
        media_group = get_media_group_by_id(media_group_id)
        debug(media_group)
        re_context = dict(
            request=request,
            title="鱼丸札记",
            media_group=media_group,
        )
        return templates.TemplateResponse(
            "admin/admin_mediagroup_detail.jinja2", re_context
        )
    return RedirectResponse(url=configs.LOGIN_PAGE)
