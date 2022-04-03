#!/usr/bin/env python
#encoding:utf-8

import configs

from fabric import Connection, task

from app.sqls import engine, Base
from app.sqls.photo import Photo

c = Connection(configs.DEPLOY_ENV_URI)



@task
def initdevdb(c):
    print("开始删除【开发环境】数据库")
    Base.metadata.drop_all(bind=engine)
    print("成功删除【开发环境】数据库")
    print("开始创建【开发环境】数据库")
    Base.metadata.create_all(bind=engine)
    print("成功创建【开发环境】数据库")



