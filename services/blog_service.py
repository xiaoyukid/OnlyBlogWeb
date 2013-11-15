#!/usr/bin/env python
#coding=utf-8
from configs import db
from models.blog import Blog

__author__ = 'tonghs'
'''
博客配置模型
'''


class BlogService:
    r = None

    def __init__(self):
        self.r = db.r

    def get_blog(self):
        """
        获取博客名和副标题
        """
        obj = self.r.hgetall(db.H_BLOG)
        blog = Blog(name=obj[db.BLOG_NAME], title=obj[db.BLOG_TITLE], password=obj[db.BLOG_PASSWORD])

        return blog

    def set_blog(self, blog):
        self.r.hmset('blog', blog.__dict__)