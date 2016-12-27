#!/usr/bin/python

sum = lambda arg1, arg2, arg3=0: arg1 + arg2 + arg3;

# Now you can call sum as a function
print "Value of total : ", sum(10, 20, 30)
print "Value of total : ", sum(20, 20)