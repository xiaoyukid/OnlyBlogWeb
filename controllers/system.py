#coding=utf-8
from models.blog import Blog
from models.param import Param
from configs.renders import *
from services.blog_service import BlogService

__author__ = 'Administrator'


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


class login:
    def GET(self):
        params = Param(title='登录')

        return render.login(params)

    def POST(self):
        params = Param()
        data = web.input()
        password = data.password

        if password == params.blog.password:
            web.ctx.session.is_login = True
            ret = web.seeother('/admin')
        else:
            params.message = '登录错误'
            params.other = {'password': password}
            params.title = '登录'
            ret = render.login(params)

        return ret

class logout:
    def GET(self):
        web.ctx.session.is_login = False
        params = Param(title='登录')

        return render.login(params)