#!/usr/bin/env python
#coding=utf-8
import web

__author__ = 'tonghs'
'''
renders
'''


base_render = web.template.render('templates/', base='base')
render = web.template.render('templates/')
admin_base_render = web.template.render('templates/', base='admin_base')

