import telepot
import datetime
from pytz import timezone, utc
KST = timezone('Asia/Seoul')
now = datetime.datetime.utcnow()
now = utc.localize(now).astimezone(KST)


def telebot(start1,start2):



    year  = datetime.datetime.today().year
    month = datetime.datetime.today().month
    day   = datetime.datetime.today().day 
    week = ['월','화','수','목','금','토','일']
    w_num = datetime.datetime.today().weekday()
    w_day = week[w_num]
    left1 = datetime.datetime.now() -  datetime.datetime(start1[0], start1[1], start1[2])
    left2 = datetime.datetime.now() -  datetime.datetime(start2[0], start2[1], start2[2])
    left_days1 = left1.days +1
    left_days2 = left2.days +1



    word = """
[불기 %d년 %d월 %d일 %s요일]

정토행자 만일결사중 제10차 천일결사 
제1차 백일기도 %d일째 기도
2차 기도하는 일공일 %d일째 기도

🙏나는 행복을 전하는 수행자입니다.

https://pray.jungto.org
""" % (year + 544, month, day, w_day,left_days1,left_days2)


    chat_id = '-399667322'
    my_token = '1210478577:AAFZTeyvx3DJU4b6WFzg9J6IhxnA4myEmrQ'
    bot = telepot.Bot(my_token)
    bot.sendMessage(chat_id, word)




    return




start1 = [2020, 3,  9]
start2 = [2020, 3, 25]
telebot(start1,start2)

