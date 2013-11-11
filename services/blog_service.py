#!/usr/bin/env python
#coding=utf-8
from models.blog import Blog
from utils.db_util import DBUtil

__author__ = 'tonghs'
'''
博客配置模型
'''


class BlogService:
    db_util = None

    def __init__(self):
        self.db_util = DBUtil()

    def get_config(self, config_name):
        """
        获取博客配置
        """
        return self.db_util.r.hget('blog:ids', config_name)

    def get_blog(self):
        """
        获取博客名和副标题
        """
        obj = self.db_util.r.hgetall('blog')
        blog = Blog(name=obj['name'], sub_title=obj['sub_title'], username=obj['username'], password=obj['password'])

        return blog