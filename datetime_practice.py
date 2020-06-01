import datetime
from pytz import timezone, utc


KST = timezone('Asia/Seoul')

now = datetime.datetime.utcnow()




now = utc.localize(now).astimezone(KST)



print(now)
