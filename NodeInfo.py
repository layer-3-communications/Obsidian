#o The module will connect to the database or csv, pull a particular set of data, 
# and sets all data to a list to be used

import sqlite3
import csv

# connection to the database and get infomation
def db(dbPath, hostGrp):
    
    # build sql query

    sqlQry = "SELECT hostName, monIP, realIP, manuf, snmp, comString, monName from %s;" % (hostGrp) 

    # creaat connection and query information
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute(sqlQry)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # populate list from query results
    nodeList = [list(i) for i in results]
    
    return nodeList


def csv(dbPath, hostGrp):

    with open('nodes.csv', 'rb') as f:
            reader = csv.reader(f)
            nodeList = list(reader)
    
    return nodeList
