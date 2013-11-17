#!/usr/bin/env python
#coding=utf-8
from services.post_service import PostService

__author__ = 'tonghs'
'''

'''
import web
import json
from models.param import Param
from services.category_service import CategoryService


base_render = web.template.render('templates/', base='base')
render = web.template.render('templates/')
admin_base_render = web.template.render('templates/', base='admin_base')


class category:
    def GET(self, name, page=1, ret_type=0):
        id = CategoryService().get_category_by_name(name)
        list_post_ids = CategoryService().get_post_ids_by_category(id, page)
        list_post = PostService().get_posts_by_ids(list_post_ids, ret_type)
        params = Param(current_page=int(page), post_list=list_post, title=name, special=name)
        if ret_type:
            return json.dumps(list_post)
        else:
            return base_render.category(params)


class get_category:
    def GET(self):
        categories = CategoryService().get_category()

        return json.dumps(categories)