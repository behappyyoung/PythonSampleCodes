#!/usr/bin/python


def changeme( mylist ):
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist


def changeme2( mylist2 ):
   mylist2 = [1,2,3,4];          # This would assig new reference in mylist2
   print "Values inside the function: ", mylist2
   return

mylist2 = [10,20,30];
changeme2( mylist2 );
print "Values outside the function: ", mylist2