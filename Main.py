# MAIN

import datetime
from ctypes import c_bool

print("Log: Start Python")

def date():
    nowDate = datetime.datetime.now()
    return [nowDate.year, nowDate.month, nowDate.day, nowDate.hour, nowDate.minute, nowDate.second]

currentTime = date()
print(currentTime)

print("Hallo Flo")
