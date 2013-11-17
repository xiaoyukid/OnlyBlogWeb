#!/usr/bin/env python
#coding=utf-8
import json
from controllers.base import Base
from models.param import Param
from configs.renders import *
from services.post_service import PostService

__author__ = 'tonghs'
'''
视图
'''

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