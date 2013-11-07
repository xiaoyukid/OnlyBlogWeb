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