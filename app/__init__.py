#!/usr/bin/env python
# encoding:utf-8
from app.schmas.user import UserLogin
import configs
from devtools import debug
from hashlib import md5
from app.misc.public import templates

from fastapi import FastAPI, Request, Depends, Response
from fastapi.staticfiles import StaticFiles
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


from fastapi_login import LoginManager
from starlette.responses import RedirectResponse

from app.routers import media
from app.routers import user

from app.service.user import query_user_by_email, user_load_query_by_email


lm = LoginManager(
    configs.SECRET, "/login", use_cookie=True, cookie_name="fishball-cookie-name"
)

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=configs.DATABASE_URI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=configs.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(media.media_router)
app.include_router(user.user_router)

app.mount("/statics", StaticFiles(directory=configs.STATIC_FILES_PATH), name="static")
app.mount("/upload", StaticFiles(directory=configs.UPLOADS_FILES_PATH), name="upload")






@lm.user_loader()
def query_user(user_email: str):
    return user_load_query_by_email(user_email)

@app.get("/", name="index")
def index_handle(request: Request):
    return RedirectResponse(url=app.url_path_for("media_index"))


@app.get("/login")
def login_handle(request: Request):
    re_context = dict(
        request=request,
    )
    return templates.TemplateResponse("user/login.jinja2", re_context)

@app.post("/login", name='login')
def login(data: UserLogin):
    password = data.password
    email = data.username
    content = dict(status='ok')
    debug(email)
    debug(password)
    user = query_user_by_email(email)
    if not user:
        debug("no user")
        raise InvalidCredentialsException
    elif md5(str.encode(password)).hexdigest() != user.hashed_password:
        raise InvalidCredentialsException
    response = JSONResponse(content=content)
    token = lm.create_access_token(data=dict(sub=user.email))
    lm.set_cookie(response, token)
    return response


@app.get("/logout", name='logout')
def logout():
    response = RedirectResponse(url=app.url_path_for('login'))
    response.delete_cookie("fishball-cookie-name")
    return response



lm.useRequest(app)