# gets host group and alias
def generateInventory(c, hostGroup, genDir):

    # database quary
    dbQuary = "SELECT monName, hostName, monIP, realIP, manuf, numDevices, model, softVer, serials FROM '%s' ORDER BY monName" % hostGroup

    # create file name and open it
    invFile = genDir + "/inventory-%s.csv" %  hostGroup
    invList = open(invFile, "w")

    # private variables
    output = ''

    # host group information from csv mapping to variables
    for row in c.execute(dbQuary):
        monName = row[0]
        hostName = row[1]
        monIP = row[2]
        realIP = row[3]
        manuf = row[4]
        numDev = row[5]
        model = row[6]
        version = row[7]
        serials = row[8]


        # generate cofig output and write to file
        if "L3C" not in hostName:
                output = generateInv(monName, hostName, monIP, realIP, manuf, numDev, model, version, serials)        
                invList.write(output)
                output = ''

    #close file
    invList.close()


# generate inventory list
def generateInv(monName, hostName, monIP, realIP, manuf, numDev, model, version, serials):
    
    invList = "%s,%s,%s,%s,%s,%s,%s,%s,%s,\n" % (monName, hostName, monIP, realIP, manuf, numDev, model, version, serials)

    return invList


