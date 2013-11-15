#coding=utf-8
from models.blog import Blog

__author__ = 'Administrator'
from services.blog_service import BlogService
import web


render = web.template.render('templates/')


class install:
    def GET(self):
        return render.install()

    def POST(self):
        data = web.input()
        name = data.name
        title = data.title
        password = data.password

        blog = Blog(name=name, title=title, password=password)
        BlogService().set_blog(blog)

        return web.seeother('/')


class faviconICO(object):
   def GET(self):
       return web.seeother('/static/images/favicon.ico')