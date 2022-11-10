from pytz import timezone
from datetime import datetime
today = datetime.now(timezone('Asia/Seoul'))

m = today.month

if 3 <= m <= 5 :
  print("봄")
if 7 <= m <= 9 :
  print("여름")
if 10 <= m <=11 :
  print("가을")
if (12 == m) or (1 == m):
  print("겨울")
  