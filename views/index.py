#!/usr/bin/env python
#coding=utf-8
import web
from services.blog_service import BlogService
from services.menu_service import MenuService
from services.post_service import PostService
__author__ = 'tonghs'
'''
视图
'''



render = web.template.render('templates/')


class index:
    def GET(self, page):
        if page is None or page == '':
            page = 1

        post_list = PostService().get_posts(page)
        menu_list = MenuService().get_menus(page)
        blog = BlogService().get_blog_name_and_sub_title()
        params = {'blog': blog, 'post_list': post_list, 'menu_list': menu_list}

        return render.index(params)


class faviconICO(object):
   def GET(self):

       return web.seeother('/static/images/favicon.ico')