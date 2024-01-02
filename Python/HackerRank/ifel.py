import math
import os
import random
import re
import sys

n = 8

# if __name__ == '__main__':
#     n = int(input().strip())
if n % 2 == 1:
    print('Weird')
elif n % 2 == 0 and n in range(2, 5):
    print('Not Weird')
elif n % 2 == 0 and n in range(6, 20): #when doing range in an if el, make sure to put the 'variable in' then the range
    print('Weird')
elif n % 2 == 0 and n >= 21:
    print('Not Weird')