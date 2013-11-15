#!/usr/bin/env python
#coding=utf-8
from configs import db
from configs import settings
from models.post import Post

__author__ = 'tonghs'
'''
文章服务
用于文章的管理
'''


class PostService:
    r = None

    def __init__(self):
        self.r = db.r

    def get_posts(self, page):
        """
        获取所有文章

        @param page 当前页
        """
        start = (int(page) - 1) * int(settings.PAGE_SIZE)
        end = int(page) * int(settings.PAGE_SIZE) - 1

        list_ids = self.r.lrange(db.L_POST_IDS, start, end)

        list_post = []
        for post_id in list_ids:
            dic_post = self.r.hgetall(db.H_POST % post_id)
            post = Post(id=post_id, title=dic_post[db.H_POST_TITLE], content=dic_post[db.H_POST_CONTENT])
            list_post.append(post)

        return list_post

    def get_post(self, post_id):
        """
        根据ID获取post
        """
        dic_post = self.r.hgetall(db.H_POST % int(post_id))
        post = Post(id=post_id, title=dic_post[db.H_POST_TITLE], content=dic_post[db.H_POST_CONTENT])

        return post

    def add_post(self, post):
        """
        添加文章
        """
        pipe = self.r.pipeline()

        #获取ID
        id = str(self.r.incr(db.STR_POST_COUNT))

        #添加/更新tag
        tag_score = pipe.zincrby('tags', post.tag)

        #tag文章列表修改
        #pipe.lpush('tag:' + post['tag'], id)

        #添加/更新分类
        #cate_score = pipe.zincrby('categories', post['category'])

        #文章分类列表修改
        #pipe.lpush('category:' + post['category'], id)

        #文章ID列表
        pipe.lpush(db.L_POST_IDS, id)

        #增加文章
        pipe.hmset(db.H_POST % int(id), post.__dict__)

        pipe.execute()

        return id

    def update_post(self, post):
        """
        添加文章
        """

        #增加文章
        self.r.hset(db.H_POST % int(post.id), 'title', post.title)
        self.r.hset(db.H_POST % int(post.id), 'content', post.content)

        return post.id