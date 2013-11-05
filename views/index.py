#!/usr/bin/env python
#coding=utf-8
import web
import json
from models.param import Param
from services.category_service import CategoryService
from services.post_service import PostService
from services.tag_service import TagService

__author__ = 'tonghs'
'''
视图
'''

render = web.template.render('templates/', base='base')


class index:
    def GET(self, page=1, ret_type=0):
        post_list = PostService().get_posts(page)
        params = Param(current_page=int(page), post_list=post_list)
        if ret_type:
            return json.dumps(post_list)
        else:
            return render.index(params)


class faviconICO(object):
   def GET(self):
       return web.seeother('/static/images/favicon.ico')


class post:
    def GET(self, post_id):
        post = PostService().get_post(post_id)
        params = Param(post=post, title=post['title'])

        return render.post(params)


class category:
    def GET(self, name, page=1, ret_type=0):
        post_list = CategoryService().get_post_by_category(name, page)
        params = Param(current_page=int(page), post_list=post_list, title=name, special=name)
        if ret_type:
            return json.dumps(post_list)
        else:
            return render.category(params)


class tag:
    def GET(self, name, page=1, ret_type=0):
        post_list = TagService().get_post_by_tag(name, page)
        params = Param(current_page=int(page), post_list=post_list, title=name, special=name)
        if ret_type:
            return json.dumps(post_list)
        else:
            return render.tag(params)