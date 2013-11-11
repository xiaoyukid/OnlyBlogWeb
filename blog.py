#!/usr/bin/env python
#coding=utf-8
from configs import urls

__author__ = 'tonghs'

import web

urls = urls.urls
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'username': ''})

def session_hook():
    web.ctx.session = session

app.add_processor(web.loadhook(session_hook))

if __name__ == '__main__':
    app.run()