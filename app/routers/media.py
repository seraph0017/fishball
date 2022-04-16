#!/usr/bin/env python
# encoding:utf-8


import configs
from app.misc.public import templates
from fastapi import APIRouter, Request, UploadFile, Form
from fastapi_sqlalchemy import db
from app.schmas.media import MediaEditSchema, MediaGroupCreateSchema
from starlette.responses import RedirectResponse


from app.service.media import (
    convert_page_to_skip_limit,
    count_age,
    create_media_group,
    get_media_groups_by_user_type,
    get_total_page_num,
    upload_media,
    get_medias,
    get_media_by_id,
    edit_media,
    parse_media_recent,
    get_media_group_by_id,
)


from devtools import debug
from app.logger import logger as l


media_router = APIRouter(prefix="/medias", tags=["medias"])

media_group_router = APIRouter(prefix="/mediagroup", tags=["mediagroup"])


@media_group_router.get("/{media_group_id}", name="media_group_index")
def media_group_index_handle(
    request: Request, media_group_id: int = 1, page_num: int = 1
):
    debug(request.state.user)
    if request.state.user:
        skip, limit = convert_page_to_skip_limit(page_num)
        mediaobjs = parse_media_recent(get_medias(media_group_id, skip, limit))
        total_page_num = get_total_page_num(media_group_id)
        f_age, c_age = count_age()
        media_groups = get_media_groups_by_user_type(request.state.user.user_type)
        current_mediagroup = get_media_group_by_id(media_group_id)
        debug(current_mediagroup)
        re_context = dict(
            request=request,
            title="鱼丸札记",
            project_name="鱼丸札记",
            mediaobjs=mediaobjs,
            f_age=f_age,
            c_age=c_age,
            now_page_num=page_num,
            total_page_num=total_page_num,
            current_user=request.state.user,
            current_mediagroup=current_mediagroup,
            media_groups=media_groups,
        )
        return templates.TemplateResponse("media/media_base.jinja2", re_context)
    return RedirectResponse(url=configs.LOGIN_PAGE)

@media_group_router.post("/", name="media_group_add")
def media_group_add_handle(request: Request, media_group_create: MediaGroupCreateSchema):
    if request.state.user:
        create_media_group(media_group_create)
        return "ok"
    return RedirectResponse(url=configs.LOGIN_PAGE)


@media_router.post("/", name="media_add")
async def media_add_handle(
    request: Request,
    mediafile: UploadFile,
    user_id: int = Form(...),
    media_group_id: int = Form(...),
):
    if request.state.user:
        contents = await mediafile.read()
        return upload_media(user_id, media_group_id, mediafile.filename, contents)
    return RedirectResponse(url=configs.LOGIN_PAGE)


@media_router.get("/{media_id}", name="media_detail")
def media_detail_handle(request: Request, media_id: int):
    if request.state.user:
        media = get_media_by_id(media_id)
        debug(media)
        re_context = dict(
            request=request,
            title="鱼丸札记",
            project_name="鱼丸札记",
            media=media,
        )
        return templates.TemplateResponse("media/media_detail.jinja2", re_context)
    return RedirectResponse(url=configs.LOGIN_PAGE)


@media_router.patch("/{media_id}", name="media_edit")
def media_edit_handle(request: Request, media_id: int, mediaEdit: MediaEditSchema):
    if request.state.user:
        a = edit_media(media_id, mediaEdit)
        debug(a)
        return "ok"
    return RedirectResponse(url=configs.LOGIN_PAGE)
