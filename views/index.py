#coding=utf-8
__author__ = 'Administrator'
import web

import utils


render = web.template.render("templates/")


class index:
    def __init__(self):
        pass

    def GET(self):
        a = utils.common()


        return render.index()