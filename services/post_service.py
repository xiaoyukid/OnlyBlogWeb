#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonghs'
'''
文章服务
用于文章的管理
'''

from utils.db_util import DBUtil
import configs
from models.post import Post


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

        list_ids = self.db_util.get_object_ids('post', start, end)

        list_post = []
        for post_id in list_ids:
            dic_post = self.db_util.get_hash_obj_by_id('post', post_id)
            post = Post(post_id, dic_post['title'], dic_post['content'])
            list_post.append(post)

        return list_post