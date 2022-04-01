#!/usr/bin/env python
#encoding:utf-8

from app.misc.public import templates
from fastapi import APIRouter, Request

photo_router = APIRouter(
    prefix="/photos",
    tags=["photos"]
)


@photo_router.get("/")
def photo_index_handle(request: Request):
    return templates.TemplateResponse("_base.html", {"request":request})