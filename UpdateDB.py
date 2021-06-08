# This module opens the inventory.csv file along with a database connection
# to monitoring nodes and updates serial, version, and model based on 

import csv
import sqlite3

def run(gathDir, dbPath, hostGrp):

    # private variables initiated
    hostName = ''
    monIP = ''
    realIP = ''
    vendor = ''
    model = ''
    version = ''
    serials = ''
    monName = ''	
    numDevices = ''
    sqlQry = ""

    # open csv file and add infomation into a list
    with open(gathDir + '/inventory.csv', 'r') as f:
            reader = csv.reader(f)
            nodeList = list(reader)

    # creaat connection
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
     
    # maps variables and updates it correctly into the database
    for node in nodeList:
            hostName = node[0]
            monIP = node[1]
            realIP = node[2]
            vendor = node[3]
            model = node[4]
            version = node[5]
            serials = node[6]
            monName = node[7]		
            numDevices = node[8]		
            
            # build sql query
            sqlQry = "UPDATE %s SET model = '%s', softVer = '%s', serials = '%s', numDevices = '%s'  WHERE monName = '%s';" % (hostGrp, model, version, serials, numDevices, monName) 
            
            # execute query
            cursor.execute(sqlQry)
            conn.commit()
    
    # close database connection
    cursor.close()
    conn.close()
   
