#!/usr/bin/env python
# encoding:utf-8


import configs
from app.misc.public import templates
from fastapi import APIRouter, Request, UploadFile, Form
from fastapi_sqlalchemy import db
from app.schmas.media import MediaEditSchema
from app.misc.login_required import login_required
from starlette.responses import RedirectResponse


from app.service.media import (
    convert_page_to_skip_limit,
    count_age,
    get_total_page_num,
    upload_media,
    get_medias,
    get_media_by_id,
    edit_media,
    parse_media_recent,
)


from devtools import debug
from app.logger import logger as l


media_router = APIRouter(prefix="/medias", tags=["medias"])


@media_router.get("/", name="media_index")
def media_index_handle(request: Request, page_num: int = 1):
    debug(request.cookies)
    debug(request.state.user)
    if request.state.user:
        skip, limit = convert_page_to_skip_limit(page_num)
        mediaobjs = parse_media_recent(get_medias(skip, limit))
        total_page_num = get_total_page_num()
        f_age, c_age = count_age()
        re_context = dict(
            request=request,
            title="鱼丸札记",
            project_name="鱼丸札记",
            mediaobjs=mediaobjs,
            f_age=f_age,
            c_age=c_age,
            now_page_num=page_num,
            total_page_num=total_page_num,
            current_user = request.state.user,

        )
        return templates.TemplateResponse("media/media_base.jinja2", re_context)
    return RedirectResponse(url=configs.LOGIN_PAGE)


@media_router.post("/", name="media_add")
async def media_add_handle(
    request: Request, mediafile: UploadFile, user_id: int = Form(...)
):
    contents = await mediafile.read()
    return upload_media(user_id, mediafile.filename, contents)


@media_router.get("/{media_id}", name="media_detail")
def media_detail_handle(request: Request, media_id: int):
    media = get_media_by_id(media_id)
    debug(media)
    re_context = dict(
        request=request,
        title="鱼丸札记",
        project_name="鱼丸札记",
        media=media,
    )
    return templates.TemplateResponse("media/media_detail.jinja2", re_context)


@media_router.patch("/{media_id}", name="media_edit")
def media_edit_handle(request: Request, media_id: int, mediaEdit: MediaEditSchema):
    debug(111)
    debug(mediaEdit)
    a = edit_media(media_id, mediaEdit)
    debug(a)
    return "ok"
