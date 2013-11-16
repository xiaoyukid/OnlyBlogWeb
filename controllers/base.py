#coding=utf-8
import web

__author__ = 'Administrator'


class Base:
    def __init__(self):
        if not web.ctx.session.is_login:
            web.seeother('/login')