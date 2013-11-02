#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonghs'
'''
视图
'''

import web

import utils
from services.post_service import PostService


render = web.template.render('templates/')


class index:
    def GET(self, page):
        if page is None or page == '':
            page = 1

        post_list = PostService().get_posts(page)

        return render.index(post_list)


class faviconICO(object):
   def GET(self):

       return web.seeother('/static/images/favicon.ico')