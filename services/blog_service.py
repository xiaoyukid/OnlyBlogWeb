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
        return self.db_util.get_hash_attr('blog', config_name)

    def get_blog_name_and_sub_title(self):
        """
        获取博客名和副标题
        """
        obj = self.db_util.get_blog_name_and_sub_title()
        blog = Blog(obj[0], obj[1])

        return blog