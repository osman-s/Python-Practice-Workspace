from datetime import datetime
import time
print(time.time())


def send_emails():
    for i in range(10000):
        pass


# 9. Working with Timestamps
start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)

# Working with DateTimes

dt = datetime(2018, 1, 1)
dt = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))
