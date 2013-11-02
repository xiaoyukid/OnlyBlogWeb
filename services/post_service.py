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
        '''
        获取所有文章
        '''
        start = (int(page) - 1) * int(configs.PAGE_SIZE)
        end = int(page) * int(configs.PAGE_SIZE) - 1

        list_ids = self.db_util.get_object_ids('posts', start, end)

        list_post = []
        for post_id in list_ids:
            post = self.db_util.get_object_by_id('post', post_id)
            list_post.append(post)

        return list_post