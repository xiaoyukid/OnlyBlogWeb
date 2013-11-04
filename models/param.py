#!/usr/bin/env python
#coding=utf-8
from services.blog_service import BlogService
from services.category_service import CategoryService

__author__ = 'tonghs'
'''
参数模型
'''


class Param:
    title = None
    blog = None
    post = None
    post_list = None
    menu_list = None

    def __init__(self, post=None, post_list=None, title=None):
        self.blog = BlogService().get_blog()
        self.menu_list = menu_list = CategoryService().get_menus()

        self.post = post
        self.post_list = post_list
        if title is None:
            blog = BlogService().get_blog()
            self.title = blog.name + " | " + blog.sub_title

        else:
            self.title = title


