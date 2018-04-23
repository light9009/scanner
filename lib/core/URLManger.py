#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 17:50
# @Author  : Light
# @Site    : 
# @File    : URLManger.py
# @Software: PyCharm Community Edition

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class URLManger(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) >0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url



if __name__ == "__main__":
    pass



