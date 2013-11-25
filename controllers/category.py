#!/usr/bin/env python
#coding=utf-8
from services.post_service import PostService
import json
from models.param import Param
from services.category_service import CategoryService
from configs.renders import *
__author__ = 'tonghs'
'''

'''


class category:
    def GET(self, name, page=1, ret_type=0):
        id = CategoryService().get_category_by_name(name)
        list_post = []
        params = Param(current_page=int(page), title=name, special=name)
        # 分类存在
        if id:
            list_post_ids = CategoryService().get_post_ids_by_category(id, page)
            list_post = PostService().get_posts_by_ids(list_post_ids, ret_type)
            params.post_list = list_post
        if int(ret_type):
            return json.dumps(list_post)
        else:
            return base_render.category(params)


class get_category:
    def GET(self):
        categories = CategoryService().get_category()

        return json.dumps(categories)