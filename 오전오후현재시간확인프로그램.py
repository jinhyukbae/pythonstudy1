from pytz import timezone
from datetime import datetime
today = datetime.now(timezone('Asia/Seoul'))

print(f"{today.hour}시{today.minute}분{today.second}초 입니다.")

if today.hour < 12:
  print("오전")
if today.hour >= 12:
  print("오후")

