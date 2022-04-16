#!/usr/bin/env python
#encoding:utf-8

import configs

from fabric import Connection, task

from app.sqls import engine, Base
from app.sqls.media import Medias, MediaGroups
from app.sqls.user import Users

from app.schmas.user import UserCreate
from app.schmas.media import MediaGroupCreateSchema

from app.service.user import create_user
from app.service.media import create_media_group

from fastapi_sqlalchemy import db

c = Connection(configs.DEPLOY_ENV_URI)



@task
def initdevdb(c):
    print("开始删除【开发环境】数据库")
    Base.metadata.drop_all(bind=engine)
    print("成功删除【开发环境】数据库")
    print("开始创建【开发环境】数据库")
    Base.metadata.create_all(bind=engine)
    print("成功创建【开发环境】数据库")
    print("开始创建管理员")
    uc = UserCreate(
        email="seraph0017@hotmail.com",
        user_type=0,
        nick_name="燕斌",
        hashed_password="bdf35c538f32eab963a3de0ac947c5a9",
        photo_url="http://wwwwwww",
        is_superuser=True,
    )

    mg = MediaGroupCreateSchema(
        title="默认相册",
        description="默认1234567",
    )
    mg2 = MediaGroupCreateSchema(
        title="精选相册",
        description="默认1234567",
        group_level=1,
    )
    with db():
        create_user(uc)
        create_media_group(mg)
        create_media_group(mg2)
    print("成功创建管理员")




@task
def deploy(c):
    pass 



@task
def inituser(c):
    Base