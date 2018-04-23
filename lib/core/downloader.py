#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 17:56
# @Author  : Light
# @Site    : 
# @File    : downloader.py
# @Software: PyCharm Community Edition

import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
from config import *


class Downloader(object):
    def get(self,url):

        headers = {}
        try:
            headers['User-Agent'] = USER_AGENT[0]
            resp = requests.get(url,timeout=10,headers=headers)
            return resp.content if resp.status_code == 200 else None
        except Exception as e:
            return None


    def post(self,url, data):
        resp = requests.post(url, data)
        return resp.content


    def download(self,url,contents):
        if url is None:
            return None

        _tmp = {}
        _tmp['url'] = url
        _tmp['html'] = self.get(url)

        contents.append(_tmp)




if __name__ == "__main__":
    pass



