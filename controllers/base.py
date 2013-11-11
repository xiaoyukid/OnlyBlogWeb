#coding=utf-8
import web

__author__ = 'Administrator'


class Base:
    def __init__(self):
        if web.ctx.session.username == '':
            web.seeother('/login')