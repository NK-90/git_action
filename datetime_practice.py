import datetime
from datetime import timezone,timedelta
import time
from pytz import timezone , utc



start1 = [2020, 3,  9]
start2 = [2020, 3, 25]

kST = timezone('Asia/Seoul')
now = datetime.datetime.now(kST)

year = int(now.strftime('%Y'))
month = int(now.strftime('%m'))
day = int(now.strftime('%d'))
w_day = ['월', '화', '수', '목', '금', '토', '일'][datetime.datetime(year,month,day).weekday()]




left1 = datetime.datetime(year, month, day) - datetime.datetime(start1[0], start1[1], start1[2])
left2 = datetime.datetime.now() - datetime.datetime(start2[0], start2[1], start2[2])

print(type(now))
print(type(datetime.datetime.now()))