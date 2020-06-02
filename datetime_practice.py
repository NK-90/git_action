import datetime
from datetime import timezone,timedelta
import time
from pytz import timezone , utc


kST = timezone('Asia/Seoul')
now = datetime.datetime.now(kST)


year  = int(now.strftime('%Y'))
month  = int(now.strftime('%m'))
day  = int(now.strftime('%d'))
hour = int(now.strftime('%H'))
min  = int(now.strftime('%M'))
sec  = int(now.strftime('%S'))

week = ['월','화','수','목','금','토','일']
w_num = datetime.datetime.today().weekday()
w_day = week[w_num]


print(w_day)
