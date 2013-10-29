#coding=utf-8
__author__ = 'Administrator'
import web
from utils.db_util import DBUtil


render = web.template.render("templates/")


class Index:
    def __init__(self):
        pass

    def GET(self):
        posts = DBUtil.get_object('post')

        for p in posts:
            a = p.title
        return render.index()