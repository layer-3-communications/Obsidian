# gets host group and alias
def generateConfig(c, hostGroup, genDir):

    # database quary
    dbQuary = "SELECT monName, realIP, monIP FROM '%s' ORDER BY monName" % hostGroup

    # create file name and open it
    srxConfigFile = genDir + "/srxOutput-%s.txt" % hostGroup
    srxConfig = open(srxConfigFile, "w")

    # host group information from csv mapping to variables
    for row in c.execute(dbQuary):
        hostName = row[0]
        realIP = row[1]
        monIP = row[2]

        # generates commands and write to file
        output = generateCommands(hostGroup, hostName, realIP, monIP)
        srxConfig.write(output)

    # close file
    srxConfig.close()

# generate commands and returns output
def generateCommands(hostGroup, hostName, realIP, monIP):
    srxOutput = "set security address-book global address %s %s/32" % (hostName, realIP) + "\n" \
    "set security address-book global address-set MONITORED-ELEMENTS address %s" % (hostName) + "\n" \
    "set security nat static rule-set MONITORED-ELEMENTS-STATIC-NATS rule %s match destination-address %s/32" % (hostName, monIP) + "\n" \
    "set security nat static rule-set MONITORED-ELEMENTS-STATIC-NATS rule %s then static-nat prefix-name %s\n" % (hostName, hostName) + "\n" \
        
    return srxOutput
