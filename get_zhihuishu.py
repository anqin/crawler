#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: get_zhihuishu.py
Author: qinan(qinan@baidu.com)
Date: 2014/10/15 22:23:29
"""

import os
import re
import string

url="curl  \"http://www.flvcd.com/parse.php?kw=http%3A%2F%2Ftv.cntv.cn%2Fvideo%2FC16724%2Fa5ca0441cf5940838b1b7f0f4e070bd7&format=high\""

output=os.popen(url)
content = output.read()
# print content
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
# print urls
downloads = set()
for link in urls:
    if link[-3:] != "mp4":
        continue
    if string.find(link, "....") != -1:
        continue
    downloads.add(link)
#     print link
for s in downloads:
    name = s[47:57].replace("/", "_") + "_" + s[-5:]
    print s, name
    cmd = "wget -O %s %s" %(name, s)
    os.popen(cmd)


