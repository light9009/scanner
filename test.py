#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 21:38
# @Author  : Light
# @Site    : 
# @File    : test.py
# @Software: PyCharm Community Edition

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from lib.core.spider import SpiderMain

def main():
    root = "http://cloudpet.io/"
    threadNum = 5
    s = SpiderMain(root, threadNum)
    s.craw()

def test(*args,**kwargs):
    print kwargs['html']
    print kwargs

def thief():
    for t in ['a','b','c','d']:
        sum = (t!='a') + (t =='c' ) +(t == 'd' ) +(t != 'd')
        if sum == 3:
            print t

if __name__ == "__main__":
    thief()
   #main()


