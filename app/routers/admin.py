#!/usr/bin/env python
#encoding:utf-8

from fastapi import APIRouter


admin_router = APIRouter(prefix="/admin", tags=["admin"])



@admin_router("/", name="admin_dashboard")
def admin_handle():
    pass

@admin_router("/user", name="admin_user_list")
def admin_user_handle():
    pass

@admin_router("/user/{user_id}", name="admin_user_detail")
def admin_user_detail_handle():
    pass

@admin_router("/media", name="admin_media_list")
def admin_user_handle():
    pass

@admin_router("/media/{media_id}", name="admin_media_detail")
def admin_media_detail_handle():
    pass