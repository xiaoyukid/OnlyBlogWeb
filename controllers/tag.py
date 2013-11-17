#!/usr/bin/env python
#coding=utf-8
import web
import json
from models.param import Param
from services.post_service import PostService

from services.tag_service import TagService

__author__ = 'tonghs'
'''
视图
'''

base_render = web.template.render('templates/', base='base')
render = web.template.render('templates/')
admin_base_render = web.template.render('templates/', base='admin_base')


class tag:
    def GET(self, name, page=1, ret_type=0):
        id = TagService().get_tag_by_name(name)
        list_post_ids = TagService().get_post_ids_by_tag(id, page)
        list_post = PostService().get_posts_by_ids(list_post_ids, ret_type)
        params = Param(current_page=int(page), post_list=list_post, title=name, special=name)
        if ret_type:
            return json.dumps(list_post)
        else:
            return base_render.category(params)


class get_tag:
    def GET(self):
        tags = TagService().get_tag()

        return json.dumps(tags)