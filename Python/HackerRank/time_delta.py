import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
  format = "%a %d %b %Y %H:%M:%S %z" #datetime format
  time1 = datetime.strptime(t1, format) #datetime.strptime converts the time based on the format
  time2 = datetime.strptime(t2, format)

  delta = time1 -time2 #difference in time

  return str(int(abs(delta.total_seconds())))
#total seconds calculates total seconds in delta
#abs takes the absolute value from above
#int converts to floating point, whole number, no decimal places
#str converts into a string to be used 