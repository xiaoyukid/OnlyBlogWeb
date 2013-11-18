#!/usr/bin/env python
#coding=utf-8
__author__ = 'Administrator'


class UnInitException(Exception):
    def __init__(self, value='博客未初始化'):
        self.value = value

    def __str__(self):
        return self.value