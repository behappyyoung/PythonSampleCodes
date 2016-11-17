import sys


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0: 
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

n = int(raw_input().strip())
print is_leap(n)

