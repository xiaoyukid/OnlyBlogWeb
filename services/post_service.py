#!/usr/bin/env python
#coding=utf-8
from configs import settings

from utils.db_util import DBUtil

__author__ = 'tonghs'
'''
文章服务
用于文章的管理
'''



class PostService:
    db_util = None

    def __init__(self):
        self.db_util = DBUtil()


    def get_posts(self, page):
        """
        获取所有文章
        """
        start = (int(page) - 1) * int(settings.PAGE_SIZE)
        end = int(page) * int(settings.PAGE_SIZE) - 1

        list_ids = self.db_util.r.lrange('post:ids', start, end)

        list_post = []
        for post_id in list_ids:
            dic_post = self.db_util.r.hgetall('post:' + post_id)
            dic_post['id'] = post_id
            list_post.append(dic_post)

        return list_post

    def get_post(self, post_id):
        """
        根据ID获取post
        """
        dic_post = self.db_util.r.hgetall('post:' + post_id)
        dic_post['id'] = post_id

        return dic_post

    def add_post(self, post):
        """
        添加文章
        """
        pipe = self.db_util.r.pipeline()

        #获取ID
        id = str(self.db_util.r.incr('post:count'))

        #添加/更新tag
        tag_score = pipe.zincrby('tags', post['tag'])

        #tag文章列表修改
        pipe.lpush('tag:' + post['tag'], id)

        #添加/更新分类
        cate_score = pipe.zincrby('categories', post['category'])

        #文章分类列表修改
        pipe.lpush('category:' + post['category'], id)

        #文章ID列表
        pipe.lpush('post:ids', id)

        #增加文章
        pipe.hmset('post:' + id, post)

        pipe.execute()

        return id

    def update_post(self, post):
        """
        添加文章
        """

        #增加文章
        self.db_util.r.hset('post:' + post['id'], 'title', post['title'])
        self.db_util.r.hset('post:' + post['id'], 'content', post['content'])

        return post['id']