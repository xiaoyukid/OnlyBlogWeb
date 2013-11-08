#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonghs'
'''
文章服务
用于文章的管理
'''

from utils.db_util import DBUtil
import configs


class PostService:
    db_util = None

    def __init__(self):
        self.db_util = DBUtil()

    def get_posts(self, page):
        """
        获取所有文章
        """
        start = (int(page) - 1) * int(configs.PAGE_SIZE)
        end = int(page) * int(configs.PAGE_SIZE) - 1

        list_ids = self.db_util.get_list_objects('post:ids', start, end)

        list_post = []
        for post_id in list_ids:
            dic_post = self.db_util.get_hash_obj('post:' + post_id)
            dic_post['id'] = post_id
            list_post.append(dic_post)

        return list_post

    def get_post(self, post_id):
        """
        根据ID获取post
        """
        dic_post = self.db_util.get_hash_obj('post:' + post_id)
        dic_post['id'] = post_id

        return dic_post

    def add_post(self, post):
        """
        添加文章
        """
        #获取ID
        id = str(self.db_util.get_incr_count('post:count'))
        #增加文章
        self.db_util.add_hash_obj('post:' + id, post)
        #文章ID列表
        self.db_util.add_to_list_obj('post:ids', id)
        #文章tag列表修改

        #文章分类列表修改


        return id