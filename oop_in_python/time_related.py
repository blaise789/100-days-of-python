import time

# print(time.ctime(1000000000))
# # epoch when the computer thinks time started
# print(time.time())
# print(time.ctime(time.time()))
# converting the time turple object
# (year,month,day,hours,minutes,secs,#day  of the week, #day of the year,dst)
time_tuple = (2020, 4, 20,4,20,0,0,0,0)
time_string=time.asctime(time_tuple)
print(time_string)