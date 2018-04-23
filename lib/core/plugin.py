#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 22:09
# @Author  : Light
# @Site    : 
# @File    : plugin.py
# @Software: PyCharm Community Edition

import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

class SpiderPlus(object):
    def __init__(self, plugin, disallow=[]):
        self.dir_exploit=[]
        self.disallow = ['__init__']
        self.disallow.extend(disallow)
        self.plugin = os.path.join(os.getcwd() ,plugin)

        #self.plugin = self.plugin = self.plugin.replace("\\", "/") if os.name == 'nt' else self.plugin
        sys.path.append(self.plugin)


    def list_plugin(self):
        def filter_func(file):
            if not file.endswith(".py"):
                return False
            for disfile in self.disallow:
                if disfile in file:
                    return False
            return True

        dir_exploit = filter(filter_func, os.listdir(self.plugin))

        return list(dir_exploit)


    def work(self, url, content):

        for _p in self.list_plugin():
            try:
                m = __import__(_p.split('.')[0])
                obj = getattr(m, 'PlusObj')
                s = obj().run(url, content)
            except Exception as e:
                print e



