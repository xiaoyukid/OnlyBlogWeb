#!/usr/bin/env python
#coding=utf-8
import web
import json
from controllers.base import Base
from models.param import Param
from services.blog_service import BlogService
from services.category_service import CategoryService
from services.post_service import PostService
from services.tag_service import TagService

__author__ = 'tonghs'
'''
视图
'''

base_render = web.template.render('templates/', base='base')
render = web.template.render('templates/')
admin_base_render = web.template.render('templates/', base='admin_base')


class index:
    def GET(self, page=1, ret_type=0):
        post_list = PostService().get_posts(page)
        params = Param(current_page=int(page), post_list=post_list)
        if ret_type:
            return json.dumps(post_list)
        else:
            return render.index(params)


class install:
    def GET(self):
        return render.install()

    def POST(self):
        data = web.input()
        name = data.name
        sub_title = data.sub_title
        blog = {'name': name, 'sub_title': sub_title}
        BlogService().set_blog(blog)

        return web.seeother('/')


class faviconICO(object):
   def GET(self):
       return web.seeother('/static/images/favicon.ico')

class login:
    def GET(self):
        params = Param(title='登录')

        return render.login(params)

    def POST(self):
        params = Param()
        data = web.input()
        username = data.username
        password = data.password

        if username == params.blog.username and password == params.blog.password:
            web.ctx.session.username = username
            ret = web.seeother('/admin')
        else:
            params.message = '登录错误'
            params.other = {'username': username, 'password': password}
            params.title = '登录'
            ret = render.login(params)

        return ret

class logout:
    def GET(self):
        web.ctx.session.username = ''
        params = Param(title='登录')

        return render.login(params)


class admin(Base):
    def GET(self):
        params = Param()

        return admin_base_render.admin(params)


class post:
    def GET(self, post_id):
        post = PostService().get_post(post_id)
        params = Param(post=post, title=post['title'])

        return base_render.post(params)


class category:
    def GET(self, name, page=1, ret_type=0):
        post_list = CategoryService().get_post_by_category(name, page)
        params = Param(current_page=int(page), post_list=post_list, title=name, special=name)
        if ret_type:
            return json.dumps(post_list)
        else:
            return base_render.category(params)


class tag:
    def GET(self, name, page=1, ret_type=0):
        post_list = TagService().get_post_by_tag(name, page)
        params = Param(current_page=int(page), post_list=post_list, title=name, special=name)
        if ret_type:
            return json.dumps(post_list)
        else:
            return base_render.tag(params)


class add_post:
    def GET(self):
        data = web.input()
        title = data.title
        content = data.content
        category = data.category
        tag = data.tag

        post = {'title': title, 'content': content, 'category': category, 'tag': tag}
        id = PostService().add_post(post)

        return id;


class update_post:
    def GET(self):
        data = web.input()
        title = data.title
        content = data.content
        category = data.category
        tag = data.tag
        id = data.id

        post = {'id': id, 'title': title, 'content': content, 'category': category, 'tag': tag}
        id = PostService().update_post(post)

        return id;