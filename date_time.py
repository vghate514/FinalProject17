import datetime #7 hours behind UTC
import time #25200 seconds behind UTC
from location import *

year = int(datetime.datetime.now().strftime("%y"))
month_init = int(datetime.datetime.now().strftime("%m"))
m_count = 0
days_passed = 0
while m_count <= month_init-1:
    if m_count == 2:
        if year % 4 == 0:
            days_passed += 29
        else:
            days_passed += 28
        m_count += 1
    elif m_count in [4,6,9,11]:
        days_passed += 30
        m_count += 1
    elif m_count in [1,3,5,6,7,8,10,12]:
        days_passed += 31
        m_count += 1
    else:
        m_count += 1
        continue


day_years = 0
for x in range(1,year+1):
    if x % 4 == 0:
        day_years += 366
    else:
        day_years += 365

days = (int(datetime.datetime.now().strftime("%d")) + days_passed + day_years-1)
decimal_hours = (int(datetime.datetime.now().strftime("%H")) - 7) + (int(datetime.datetime.now().strftime("%M"))/60)

#Conversion from J2000 to Local Sidereal Time (LST)
lst_time = 100.46 + 0.985647*days + lon + 15*decimal_hours

while lst_time not in range(0,361):
    if lst_time < 0:
        lst_time += 360
        continue
    elif lst_time > 360:
        lst_time -= 360
        continue
    else: continue

import math as m
print(m.asin(0.5))
