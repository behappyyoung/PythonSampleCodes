# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "young.park"


if __name__ == "__main__":
    print "DB access"

import MySQLdb
import sys

def getDBconn():
    
    try:
        conn = MySQLdb.connect (
                                host = "localhost",
                                user = "young",
                                passwd = "young",
                                db = "young")
                                
        return conn
    
    except MySQLdb.Error, e:
        print  "Error %d: %s" % (e.args[0], e.args[1])
        result = null
    
    return result
def getQuery(query):
    result =""
    try:
        dbConn = getDBconn();
        if(dbConn):
            cursor = dbConn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            return data
            dbConn.close()
        else:
            result = " DB Error"

    except MySQLdb.Error, e:
        result =  "Error %d: %s" % (e.args[0], e.args[1])
    return result

def PrintQuery(query):
    result =""
    try:
        dbConn = getDBconn();
        if(dbConn):
            cursor = dbConn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            for row in data:
                column = ""
                for col in row:
                    column +=  str(col) + ","
                result += column + "\n"
            dbConn.close()
        else:
            result = " DB Error"

    except MySQLdb.Error, e:
        result =  "Error %d: %s" % (e.args[0], e.args[1])
    return result

def commitQuery(query):
    result = ""
    try:
        dbConn = getDBconn();
        if(dbConn):
            cursor = dbConn.cursor()
            try:
                print query
                cursor.execute(query)
                dbConn.commit()
                result = "commit success"
            except MySQLdb.Error, e:
                dbConn.rollback()
                result = "db commit failed query %s -  %d: %s" % ( query, e.args[0], e.args[1])
            dbConn.close()
        else:
            result = " DB Error"
    except MySQLdb.Error, e:
        result =  "Error %d: %s" % (e.args[0], e.args[1])
    return result


##print "connected to the database"
