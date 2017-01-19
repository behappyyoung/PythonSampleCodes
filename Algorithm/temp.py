meal = float(raw_input().strip())
tip = int(raw_input().strip())
tax = int(raw_input().strip())
t = meal + (meal*tip)/100 + (meal*tax)/100
print t
print 'The total meal cost is %s dollars.'% int(round(t))