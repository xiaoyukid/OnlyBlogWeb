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
    special = None
    post_list = None
    menu_list = None
    message = None
    other = None

    def __init__(self, special='',current_page=1, message='', other=None, post=None, post_list=None, title=None):
        #博客相关信息
        self.blog = BlogService().get_blog()
        self.special = special
        #当前页
        self.current_page = current_page
        self.message = message
        #菜单列表
        self.menu_list = CategoryService().get_menus()
        self.other = other
        self.post = post
        self.post_list = post_list
        #页面标题
        if title is None:
            title_tmp = (self.blog.name, self.blog.sub_title)
        else:
            if type(title) != str:
                title = title.encode("utf-8")
            title_tmp = (title, self.blog.name)

        self.title = "%s | %s" % title_tmp