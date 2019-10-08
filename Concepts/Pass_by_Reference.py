#!/usr/bin/python
"""
    variables : passing by value
"""
def passing_var(n):
    n += 1
    return

v = 1
print("Values before passing_var function: %s" % v)
passing_var(v)
print("Values before passing_var function: %s" % v)

"""
    variables : passing value by return
"""
def passing_var_return(n):
    n += 1
    return n

v = 1
print("Values before passing_var_return function: %s" % v)
re_v = passing_var_return(v)
print("Values before passing_var_return function: %s" % v)
print("Values before passing_var_return function: %s" % re_v)


def changeme_valueupdate( mylist ):
   mylist[0] = 100;
   print("Values inside the changeme_valueupdate function: ", mylist)
   return

mylist = [10,20,30];
print("Values before changeme_valueupdate function: ", mylist)
changeme_valueupdate( mylist )
print("Values after changeme_valueupdate function: ", mylist)

print('\n')


def changeme_extend( mylist ):
   mylist.extend([1,2,3,4])
   print("Values inside the changeme_extend function: ", mylist)
   return

mylist = [10,20,30];
print("Values before changeme_extend function: ", mylist)
changeme_extend( mylist )
print("Values after changeme_extend function: ", mylist)

print('\n')

def changeme_reassign( mylist ):
   mylist = [1,2,3,4]          # This would assign new reference in mylist
   print("Values inside changeme_reassign the function: ", mylist)
   return

mylist = [10,20,30]
print("Values before changeme_reassign function: ", mylist)
changeme_reassign( mylist )
print("Values outside changeme_reassign function: ", mylist)