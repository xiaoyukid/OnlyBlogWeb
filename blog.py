#!/usr/bin/env python
#coding=utf-8
import configs

__author__ = 'tonghs'

import web

urls = configs.urls

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()