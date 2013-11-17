#!/usr/bin/env python
#coding=utf-8
import web
import json
from controllers.base import Base
from models.param import Param

from services.category_service import CategoryService
from services.post_service import PostService
from services.tag_service import TagService

__author__ = 'tonghs'
'''
视图
'''

base_render = web.template.render('templates/', base='base')
render = web.template.render('templates/')
admin_base_render = web.template.render('templates/', base='admin_base')


class index:
    def GET(self, page=1, ret_type=0):
        post_list = PostService().get_posts(page)
        params = Param(current_page=int(page), post_list=post_list)
        if ret_type:
            return json.dumps(post_list)
        else:
            return base_render.index(params)


class admin(Base):
    def GET(self):
        params = Param()

        return admin_base_render.admin(params)



class tag:
    def GET(self, name, page=1, ret_type=0):
        post_list = TagService().get_post_by_tag(name, page)
        params = Param(current_page=int(page), post_list=post_list, title=name, special=name)
        if ret_type:
            return json.dumps(post_list)
        else:
            return base_render.tag(params)




class get_tag:
    def GET(self):
        tags = TagService().get_tag()

        return json.dumps(tags)