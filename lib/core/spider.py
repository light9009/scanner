#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 18:33
# @Author  : Light
# @Site    : 
# @File    : spider.py
# @Software: PyCharm Community Edition

import sys
import plugin
import downloader
import URLManger

reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
from urlparse import urljoin
import threading

class SpiderMain(object):
    def __init__(self, root, threadNum):
        self.urls = URLManger.URLManger()
        self.downloader = downloader.Downloader()
        self.threadNum = threadNum
        self.root = root

    def _judge(self,domain, url):
        if(url.find(domain) != -1):
            return True
        else:
            return False

    def _get_new_urls(self, page_url, html_obj):
        new_urls = set()
        urls = html_obj.xpath("//a/@href")

        for url in urls:
            new_full_url = urljoin(page_url, url)
            if self._judge(self.root, new_full_url):
                new_urls.add(new_full_url)
        return new_urls


    def _parse(self, page_url,content):
        self.urls.add_new_url(self.root)
        if content is None:
            return
        html_obj = etree.HTML(content)
        return self._get_new_urls(page_url, html_obj)

    def craw(self):
        self.urls.add_new_url(self.root)
        while self.urls.has_new_url():
            _contents = []
            th = []
            for i in xrange(self.threadNum):
                if self.urls.has_new_url() is False:
                    break
                new_url = self.urls.get_new_url()

                print ("craw:"+new_url)
                t = threading.Thread(target=self.downloader.download, args=(new_url,_contents))
                t.start()
                th.append(t)
            for t in th:
                t.join()
            for c in _contents:
                if c is None:
                    continue

                new_urls = self._parse(new_url, c['html'])
                '''
                   插件位置;
                '''
                disallow = []
                _plugin = plugin.SpiderPlus("script", disallow)
                _plugin.work(str(new_url), str(c['html']))

                self.urls.add_new_urls(new_urls)

if __name__ == "__main__":
    pass



