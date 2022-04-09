#!/usr/bin/env python
#encoding:utf-8

import configs

from fabric import Connection, task
from fabric.api import local, settings, abort, run, cd

from app.sqls import engine, Base
from app.sqls.media import Medias
from app.sqls.user import Users

c = Connection(configs.DEPLOY_ENV_URI)



@task
def initdevdb(c):
    print("开始删除【开发环境】数据库")
    Base.metadata.drop_all(bind=engine)
    print("成功删除【开发环境】数据库")
    print("开始创建【开发环境】数据库")
    Base.metadata.create_all(bind=engine)
    print("成功创建【开发环境】数据库")




@task
def deploy(c):
    pass 