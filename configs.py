#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonghs'
'''
配置文件
项目相关配置文件
'''


from views.index import *

PAGE_SIZE = 10
HOST = 'localhost'
PORT = 6379
DB = 0

urls = (
    '/favicon.ico', faviconICO,

    '/admin', admin,
    '/admin/', admin,

    '/', index,
    '/page/(\d+)/(\d+)/', index,
    '/page/(\d+)/(\d+)', index,
    '/page/(\d+)/', index,
    '/page/(\d+)', index,

    '/post/(\d+)/', post,
    '/post/(\d+)', post,

    '/category/(.*)/page/(\d+)/(\d+)/', category,
    '/category/(.*)/page/(\d+)/(\d+)', category,
    '/category/(.*)/page/(\d+)/', category,
    '/category/(.*)/page/(\d+)', category,
    '/category/(.*)/', category,
    '/category/(.*)', category,

    '/tag/(.*)/page/(\d+)/(\d+)/', tag,
    '/tag/(.*)/page/(\d+)/(\d+)', tag,
    '/tag/(.*)/page/(\d+)/', tag,
    '/tag/(.*)/page/(\d+)', tag,
    '/tag/(.*)/', tag,
    '/tag/(.*)', tag,

    '/add_post', add_post,
    '/add_post/', add_post,

    '/update_post', update_post,
    '/update_post/', update_post,
)