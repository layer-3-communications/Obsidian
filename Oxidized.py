import Password

# gets host group and alias
def generateConfig(c, hostGroup, genDir):

    # database quary
    dbQuary = "SELECT monName, hostName, monIP, manufID FROM '%s' ORDER BY monName" % hostGroup

    # create file name and open it
    oxConfigFileDNS = genDir + "/oxDNS-%s.txt" %  hostGroup
    oxConfigDNS = open(oxConfigFileDNS, "w")
    oxConfigFile = genDir + "/oxConfig-%s.txt" %  hostGroup
    oxConfig = open(oxConfigFile, "w")

    # private variables
    output = ''

    # host group information from csv mapping to variables
    for row in c.execute(dbQuary):
        monName = row[0]
        hostName = row[1]
        monIP = row[2]
        manufID = row[3]

        if manufID is None:
            manufID = "bad"

        # generate cofig output and write to file
        if "L3C" not in hostName:
            if "bad" not in manufID:
                output = generateDNS(monIP, hostName)        
                oxConfigDNS.write(output)
                output = generateCmds(hostGroup, hostName, manufID)
                oxConfig.write(output)
                output = ''

    #close file
    oxConfigDNS.close()
    oxConfig.close()


# generate DNS output
def generateDNS(monIP, hostName):
    # create DNS for oxidied file
    
    oxDNS = "%s\t%s\n" % (monIP, hostName)

    return oxDNS


def generateCmds(hostGroup, hostName, manufID):
    # create config output
   
    cred = ''

    cred = Password.getPass(manufID)

    oxConfig = "%s:%s:%s:%s\n" % (hostGroup, hostName, manufID, cred)

    return oxConfig
