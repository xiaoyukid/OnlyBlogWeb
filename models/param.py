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
    current_page = None
    post_list = None
    menu_list = None

    def __init__(self, current_page=1, post=None, post_list=None, title=None):
        #博客相关信息
        self.blog = BlogService().get_blog()
        #当前页
        self.current_page = current_page
        #菜单列表
        self.menu_list = CategoryService().get_menus()
        self.post = post
        self.post_list = post_list
        #页面标题
        if title is None:
            self.title = self.blog.name + " | " + self.blog.sub_title
        else:
            self.title = title + " | " + self.blog.name