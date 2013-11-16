#!/usr/bin/env python
#coding=utf-8
from services.post_service import PostService
from models.post import Post
import web

__author__ = 'tonghs'
'''
文章相关
'''

base_render = web.template.render('templates/', base='base')
admin_base_render = web.template.render('templates/', base='admin_base')

class post:
    def GET(self, post_id):
        post = PostService().get_post(post_id)
        params = Param(post=post, title=post['title'])

        return base_render.post(params)


class add_post:
    def POST(self):
        data = web.input()
        title = data.title
        content = data.content
        category = data.category
        tags = data.tag.split(' ')

        post = Post(title=title, content=content, category=category, tags=tags)
        id = PostService().add_post(post)

        return id


class update_post:
    def POST(self):
        data = web.input()
        title = data.title
        content = data.content
        category = data.category
        tag = data.tag
        id = data.id

        post = Post(id=id, title=title, content=content, category=category, tags=tag)
        PostService().update_post(post)

        return id
