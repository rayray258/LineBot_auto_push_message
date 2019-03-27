import pymysql
'''

製作模板

'''
def recommend():
    conn = pymysql.connect(host='35.222.24.169',
                           port=3306,
                           user='root',
                           password='root',
                           db='news',
                           charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT url,title \
                       from test_news \
                       ORDER BY RAND() \
                       LIMIT 5"
                   )

    # 使用 fetchmany(n)方法获取n条数据.
    data = cursor.fetchmany(5)
    # print(data)
    # print(data[0][0])  # url
    # print(data[0][1])  # title
    conn.close()
    con = ""
    for i in data:
        title = i[1]
        url = i[0]
        bubble = """
        {
                "type": "bubble",
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "text",
                      "text": "%s",
                      "size": "xl",
                      "weight": "bold",
                      "wrap": true
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "text",
                          "text": "view:",
                          "flex": 0,
                          "size": "sm",
                          "gravity": "top",
                          "weight": "bold",
                          "wrap": true
                        },
                        {
                          "type": "text",
                          "text": "???",
                          "flex": 0,
                          "size": "sm",
                          "weight": "bold",
                          "wrap": true
                        }
                      ]
                    }
                  ]
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "button",
                      "action": {
                        "type": "uri",
                        "label": "內文點我",
                        "uri": "%s"
                      },
                      "color": "#52AC2F",
                      "style": "primary"
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "喜歡",
                        "data": "%s|like"
                      }
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "不喜歡",
                        "data": "%s|dislike"
                      }
                    }
                  ]
                }
              },""" % (title, url, url, url)
        con += bubble

    flexCarouselContainerJsondict= """
    {
    "type": "carousel",
        "contents": ["""+con+"""
          {
            "type": "bubble",
            "body": {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "uri",
                    "label": "See more",
                    "uri": "https://www.google.com/"
                  },
                  "flex": 1,
                  "gravity": "center"
                }
              ]
            }
          }
        ]
      }
    """
    return flexCarouselContainerJsondict


def foreign_recommend():
    conn = pymysql.connect(host='35.222.24.169',
                           port=3306,
                           user='root',
                           password='root',
                           db='news',
                           charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT news_title,news_link,img_link \
                       from hot_foreign_news \
                       ORDER BY RAND() \
                       LIMIT 5"
                   )

    # 使用 fetchmany(n)方法获取n条数据.
    data = cursor.fetchmany(5)
    # print(data)
    # print(data[0][0])  # title
    # print(data[0][1])  # url
    # print(data[0][2])  # img
    conn.close()
    con = """
   {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "國外新聞推播",
          "size": "3xl",
          "align": "center"
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "關注國外",
          "size": "xxl",
          "align": "center"
        },
        {
          "type": "text",
          "text": "提升國際觀",
          "size": "xxl",
          "align": "center"
        }
      ]
    }
  },
    """

    for i in data:
        img = i[2]
        title = i[0]
        url = i[1]
        bubble = """
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "%s",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "text",
                        "text": "%s",
                        "size": "xl",
                        "weight": "bold",
                        "wrap": true
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "內文點我",
                            "uri": "%s"
                        },
                        "color": "#52AC2F",
                        "style": "primary"
                    }
                ]
            }
        },
        """ % (img, title, url)
        con += bubble


    foreign="""
    {
        "type": "carousel",
        "contents": [
            """+con+"""
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "THIS IS GOOGLE",
                                "uri": "https://www.google.com/"
                            },
                            "flex": 1,
                            "gravity": "center"
                        }
                    ]
                }
            }
        ]
    }
    """
    return foreign


def subscription(userid):
    conn = pymysql.connect(host='35.222.24.169',
                                 port=3306,
                                 user='root',
                                 password='root',
                                 db='news',
                                 charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    # 使用 execute()  記錄使用者訂閱
    cursor.execute("select keyword \
                    from user_subscription \
                    where userid = '%s'"%(str(userid))
                    )
    data = cursor.fetchone()
    data =data[0]
    conn.commit()
    conn.close()
    con = """
        {
        "type": "bubble",
        "direction": "ltr",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "訂閱推播",
              "size": "3xl",
              "align": "center",
              "color": "#FF0000"
            }
          ]
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "訂閱內容:%s",
              "size": "xl",
              "align": "center",
              "weight": "bold"
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "text",
              "text": "每日8點推送",
              "size": "xl",
              "align": "center",
              "weight": "bold"
            }
          ]
        }
      },
        """ % (data)
    conn = pymysql.connect(host='35.222.24.169',
                           port=3306,
                           user='root',
                           password='root',
                           db='news_db',
                           charset='utf8')
    cursor = conn.cursor()
    sql = 'SELECT url,title FROM apple_news WHERE title like "%s"  ORDER BY RAND() LIMIT 5;' % (str("%" + data + "%"))
    cursor.execute(sql)
    # 使用 fetchmany(n)方法获取n条数据.
    data = cursor.fetchmany(5)
    conn.close()

    for i in data:
        title = i[1]
        url = i[0]

        bubble = """
         {
                 "type": "bubble",
                 "body": {
                   "type": "box",
                   "layout": "vertical",
                   "spacing": "sm",
                   "contents": [
                     {
                       "type": "text",
                       "text": "%s",
                       "size": "xl",
                       "weight": "bold",
                       "wrap": true
                     }
                   ]
                 },
                 "footer": {
                   "type": "box",
                   "layout": "vertical",
                   "spacing": "sm",
                   "contents": [
                     {
                       "type": "button",
                       "action": {
                         "type": "uri",
                         "label": "內文點我",
                         "uri": "%s"
                       },
                       "color": "#52AC2F",
                       "style": "primary"
                     },
                     {
                       "type": "button",
                       "action": {
                         "type": "postback",
                         "label": "喜歡",
                         "data": "%s|like"
                       }
                     },
                     {
                       "type": "button",
                       "action": {
                         "type": "postback",
                         "label": "不喜歡",
                         "data": "%s|dislike"
                       }
                     }
                   ]
                 }
               },""" % (title, url, url, url)
        con += bubble
    flexSubscription = """
     {
     "type": "carousel",
         "contents": [""" + con + """
           {
             "type": "bubble",
             "body": {
               "type": "box",
               "layout": "vertical",
               "spacing": "sm",
               "contents": [
                 {
                   "type": "button",
                   "action": {
                     "type": "uri",
                     "label": "See Google",
                     "uri": "https://www.google.com/"
                   },
                   "flex": 1,
                   "gravity": "center"
                 }
               ]
             }
           }
         ]
       }
     """
    return flexSubscription
