import telepot
import datetime
import pytz
from pytz import timezone, utc


KST = timezone('Asia/Seoul')

now = datetime.datetime.utcnow()
now.replace(tzinfo=pytz.utc)

now = utc.localize(now).astimezone(KST)


year  = datetime.datetime.today().year
month = datetime.datetime.today().month
day   = datetime.datetime.today().day


print(now)