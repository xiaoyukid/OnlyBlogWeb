#!/usr/bin/env python
#coding=utf-8
import web
from services.blog_service import BlogService
from services.category_service import CategoryService
from services.post_service import PostService
__author__ = 'tonghs'
'''
视图
'''



render = web.template.render('templates/')


class index:
    def GET(self, page=1):
        post_list = PostService().get_posts(page)
        menu_list = CategoryService().get_menus()
        blog = BlogService().get_blog_name_and_sub_title()
        params = {'blog': blog, 'post_list': post_list, 'menu_list': menu_list}

        return render.index(params)


class faviconICO(object):
   def GET(self):

       return web.seeother('/static/images/favicon.ico')


class post:
    def GET(self, post_id):
        post = PostService().get_post(post_id)
        menu_list = CategoryService().get_menus()
        blog = BlogService().get_blog_name_and_sub_title()
        params = {'blog': blog, 'post': post, 'menu_list': menu_list}

        return render.post(params)


class category:
    def GET(self, name, page=1):
        menu_list = CategoryService().get_menus()
        blog = BlogService().get_blog_name_and_sub_title()
        post_list = CategoryService().get_post_by_category(name, page)
        params = {'blog': blog, 'post_list': post_list, 'menu_list': menu_list, 'name': name}

        return render.category(params)