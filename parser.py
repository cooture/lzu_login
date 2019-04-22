"""
__author__ = 'Rankin'
__mtime__ = '2019-04-20'
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
import logging
import re
import time

from bs4 import BeautifulSoup as bs

panduan = {
    "第1节": {"chixu": 1, "start": 1},
    "上午12节": {"chixu": 2, "start": 1},
    "上午123节": {"chixu": 3, "start": 1},
    "上午1-4节": {"chixu": 4, "start": 1},
    "1-6节": {"chixu": 8, "start": 1},
    "1-8节": {"chixu": 10, "start": 1},
    "1-9节": {"chixu": 11, "start": 1},
    "第2节": {"chixu": 1, "start": 2},
    "上午234节": {"chixu": 3, "start": 2},
    "第3节": {"chixu": 1, "start": 3},
    "上午34节": {"chixu": 2, "start": 3},
    "3-6节": {"chixu": 6, "start": 3},
    "3-8节": {"chixu": 8, "start": 3},
    "3-10节": {"chixu": 10, "start": 3},
    "第4节": {"chixu": 1, "start": 4},
    "中午1节": {"chixu": 1, "start": 21},
    "中午2节": {"chixu": 1, "start": 22},
    "第5节": {"chixu": 1, "start": 5},
    "下午56节": {"chixu": 2, "start": 5},
    "下午5-7节": {"chixu": 3, "start": 5},
    "下午5-8节": {"chixu": 4, "start": 5},
    "5-10节": {"chixu": 6, "start": 5},
    "5-11节": {"chixu": 7, "start": 5},
    "5-12节": {"chixu": 8, "start": 5},
    "第6节": {"chixu": 1, "start": 6},
    "下午6-8节": {"chixu": 3, "start": 6},
    "第7节": {"chixu": 1, "start": 7},
    "下午78节": {"chixu": 2, "start": 7},
    "7-9节": {"chixu": 3, "start": 7},
    "7-10节": {"chixu": 4, "start": 7},
    "7-12节": {"chixu": 6, "start": 7},
    "第8节": {"chixu": 1, "start": 8},
    "8-10节": {"chixu": 3, "start": 8},
    "第9节": {"chixu": 1, "start": 9},
    "晚9-10节": {"chixu": 2, "start": 9},
    "晚9-11节": {"chixu": 3, "start": 9},
    "晚9-12节": {"chixu": 4, "start": 9},
    "第10节": {"chixu": 1, "start": 11},
    "第11节": {"chixu": 1, "start": 11},
    "晚11-12节": {"chixu": 2, "start": 11},
    "第12节": {"chixu": 1, "start": 12},
}
course_data = []
i_course_data = {}

def parse_course(file):

    f = open(file, 'r').read().replace("\n", '').strip()

    soup = bs(f, features="html.parser")
    course_table = soup(class_="infolist_tab")[0]
    course_table = course_table.find_all(class_='infolist_common')
    i_course_data.clear()
    for i in course_table:
        name = i.find(href=re.compile("course_detail")).string.strip()
        teacher = [item.string for item in i.find_all(href=re.compile("showTeacherInfoItem"))]
        all_time = i.table.find_all("tr")
        time = [item.get_text().split() for item in all_time]

        i_course_data["name"] = name
        i_course_data["teacher"] = teacher

        print("name:{}  name_len:{}  teacher:{}   time:{}".format(name, len(name), teacher, time))

    # time_table = soup(class_="infolist_tab")[1]
    # time_table = time_table.find_all(class_="infolist_common")
    #
    # for item_table in time_table:
    #     item_time = item_table.find_all("td")
    #     # print(item_time)
    #     print("\"{name}\" : {{ \"chixu\": {chixu} ,  \"start\" :{start} }},".format(
    #         name=item_time[1].string.strip(), chixu=len(item_time[2].string.strip().split()),
    #         jieci=item_time[2].string.strip().split(), start=item_time[2].string.strip().split()[0][1]))


if __name__ == '__main__':
    start = time.time()
    parse_course("course.html")
    print(time.time() - start)
