# gets host group and alias
def generateConfig(c, hostGroup, genDir):

    # database quary
    dbQuary = "SELECT hostName, realIP, comString FROM '%s' ORDER BY monName" % hostGroup

    # create file name and open it
    grafConfigFile = genDir + "/grafOutput-%s.txt" %  hostGroup
    grafConfig = open(grafConfigFile, "w")
	
    grafConfig.write('company: \'DCG\'\n' )
    grafConfig.write('customer_objects:\n')
    # host group information from csv mapping to variables
    for row in c.execute(dbQuary):
        hostName = row[0]
        realIP = row[1]
        community = row[2]
    
        # generate cofig output and write to file
        output = generateCommands(hostGroup, hostName, realIP, community)
        grafConfig.write(output)

    #close file
    grafConfig.close()

# generate commands
def generateCommands(hostGroup, hostName, realIP, community):
    # create the Grafana ouputs in the correct format if not part of L3
    
    grafOutput = ""
   
    if "bad" not in community:
    	grafOutput ="- real_addr: '%s'" % realIP + "\n" \
		    "  name: '%s'" % hostName + "\n" \
		    "  community: %s" % community + "\n" 

    return grafOutput
