# 主動推播 國外新聞
import linebot
import json
from linebot import LineBotApi
from linebot.models import(
    FlexSendMessage,CarouselContainer,BubbleContainer,TextSendMessage
)
from news_recommend import (
    foreign_recommend
)
import pymysql
def auto_message():
    # 打开数据库连接
    conn = pymysql.connect(host='35.222.24.169',
                           port=3306,
                           user='root',
                           password='root',
                           db='news',
                           charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT userid \
                   FROM user "
                   )
    data = cursor.fetchall()
    #  取出userid包成list
    conn.close()
    userid = []
    for user in data:
        for i in user:
            userid.append(i)
#        print(userid)
    carouselContent = CarouselContainer.new_from_json_dict(json.loads(foreign_recommend()))
    flexCarouselSendMeesage =  FlexSendMessage(alt_text="foreign", contents=carouselContent)
    line_bot_api = linebot.LineBotApi('mvdB7r737zcCXyzycwFOd6VZN8e1sbcQWkh8v6ue7nUfyU4/O/b2+ROhYazZ21pYoUSBtsnlE4L5Dfwpkdrk2lPJPxEzkdTgzkT5ycPeLZWpAtypNc8ogBLL0LdsRiM4ezuh0uqsssGkLL2aCb4IQwdB04t89/1O/w1cDnyilFU=')
    line_bot_api.multicast(userid, flexCarouselSendMeesage)

import datetime
import time
def doSth():
    auto_message()
    time.sleep(60)
def main(h , m):
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour == h and now.minute == m:
                break
            time.sleep(20)
        doSth()


main(16,0)