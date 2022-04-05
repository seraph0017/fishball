#!/usr/bin/env python
# encoding:utf-8


from app.misc.public import templates
from fastapi import APIRouter, Request, UploadFile, Form
from fastapi_sqlalchemy import db


from app.service.media import upload_media, get_medias


from devtools import debug
from app.logger import logger as l


media_router = APIRouter(prefix="/medias", tags=["medias"])



@media_router.get("/", name="media_index")
def media_index_handle(request: Request):
    medias = get_medias()
    re_context = dict(
        request=request,
        title="鱼丸札记",
        project_name="鱼丸札记",
        medias = medias
    )
    return templates.TemplateResponse("media/media_base.jinja2", re_context)


@media_router.post("/", name="media_add")
async def media_add_handle(
    request: Request, mediafile: UploadFile, user_id: int = Form(...)
):
    contents = await mediafile.read()
    return upload_media(user_id, mediafile.filename, contents)


@media_router.get("/{media_id}", name="media_detail")
def media_detail_handle(request: Request, media_id: int):
    return templates.TemplateResponse("")