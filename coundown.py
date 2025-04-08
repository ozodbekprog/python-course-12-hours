import time


my_time = int(input("Enter the time in seconds: "))


for x in reversed(range(0, my_time)):
  secund = x % 60
  minute = int(x / 60) % 60
  hours = int(x / 3600) % 24
  days = int(x / 86400) % 31
  print(f"{days:02}-{hours:02}-{minute:02}-{secund:02d}")
  # print(x)
  time.sleep(1)



# time.sleep(3)
print("times up")
