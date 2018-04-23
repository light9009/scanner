#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 21:48
# @Author  : Light
# @Site    : 
# @File    : sqlcheck.py
# @Software: PyCharm Community Edition

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from config import *
import requests
import re
import random
from lib.core.downloader import Downloader


class PlusObj(object):

    def __init__(self):
        self.downloader = Downloader()

    def run(self, url, content):

        if not url.find("?"):
            return False

        _url = url + "%29%28%22%27" #使用 )("' 让网页报错
        _content = self.downloader.get(_url)

        for (dbms, regex) in ((dbms,regex) for dbms in DBMS_ERRORS  for regex in DBMS_ERRORS[dbms]):
            if re.search(regex, _content):
                print "sql found: {}".format(url)
                return True

        content = {}
        content['origin'] = self.downloader.get(_url)
        for payload in BOOLEAN_TESTS:
            RANDINT = random.randint(0x1, 0xff)
            _url = url + payload % (RANDINT, RANDINT)
            content["true"] = self.downloader.get(_url)
            _url = url + payload % (RANDINT, RANDINT + 1)
            content["false"] = self.downloader.get(_url)
            if content["origin"] == content["true"] != content["false"]:
                print "sql found: {}".format(url)
                return True



