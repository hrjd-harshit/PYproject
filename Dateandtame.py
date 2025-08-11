from datetime import *
import time

now = datetime.now()
print(now)

yesterday = now - timedelta(days=1,minutes=5)
print(yesterday)
print(time.time())
time.sleep(3)
print(time.time())
