#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 0:37
# @Author  : Light
# @Site    : 
# @File    : cloudpet.py
# @Software: PyCharm Community Edition

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree

class PlusObj(object):
    def __init__(self):
        self.ids=[]


    def run(self,url, content):
        _tree = etree.HTML(content)
        stu = _tree.xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div/a/div/div[1]/div[2]/div/div/span/text()')

        if stu == "正在合作":
            id = _tree.xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div/a/div/div[3]/span[1]/text()')
            if id in self.ids:
                print id
            else:
                self.ids.append(id)



