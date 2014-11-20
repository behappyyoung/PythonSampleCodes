#!/usr/bin/python
print "Content-type:text/html\n\n"
import MySQLdb
import sys

try:
 conn = MySQLdb.connect (
  host = "takofirecom.ipagemysql.com",
  user = "projectm",
  passwd = "projectm",
  db = "projectm")

except MySQLdb.Error, e:
 print "Error %d: %s" % (e.args[0], e.args[1])
 sys.exit (1)

print "connected to the database"

