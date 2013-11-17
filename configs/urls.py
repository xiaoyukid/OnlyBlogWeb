#coding=utf-8

from controllers.index import *
from controllers.system import *
from controllers.post import *
from controllers.category import *
from controllers.tag import *

__author__ = 'Administrator'

urls = (
    '/favicon.ico', faviconICO,

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


    '/admin', admin,
    '/admin/', admin,

    '/login', login,
    '/login/', login,

    '/logout', logout,
    '/logout/', logout,

    '/install', install,
    '/install/', install,

    '/get_category', get_category,
    '/get_category/', get_category,

    '/get_tag', get_tag,
    '/get_tag/', get_tag,
)