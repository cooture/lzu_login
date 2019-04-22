"""
__author__ = 'Rankin'
__mtime__ = '2019-04-22'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import re

from bs4 import BeautifulSoup


a = BeautifulSoup(open("course.html"), features="html.parser")
# print(a.html.head)
for i in a.find_all(href=re.compile("course_detail")):
    print(type(i), i.get_text())


