#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 14:42
# @Author  : Light
# @Site    : 
# @File    : spider1.py
# @Software: PyCharm Community Edition

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
import requests
from lxml import etree

def dwonload(url):
    heads ={}
    heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    req = requests.get(url, headers=heads, timeout=10)
    resp = requests.get(url)
    #print resp.content
    urls = re.findall(r"(?<=href=[\"\']).+?(?=[\"\'])", resp.content)

    html = etree.HTML(resp.content)
    power = html.xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div/a/div/div[3]/span[4]/text()')
    price = html.xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div/a/div/div[1]/div[2]/div/div/span[2]/span/text()')
    id = html.xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div/a/div/div[3]/span[1]/text()')
    generate = html.xpath('//*[@id="app"]/div/main/div/div[2]/div/div/div/a/div/div[3]/span[2]/text()')

    for i in xrange(len(id)):
        if int(power[i].split(":")[1]) > 300:
            print  "{} {} {} {}".format(id[i],generate[i],power[i],price[i])




if __name__ == "__main__":
    for i in xrange(1, 30, 1):
        print i
        dwonload("http://cloudpet.io/dog/sale?page={}".format(i))



