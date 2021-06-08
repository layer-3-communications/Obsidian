# This module parses node list to separte varibles to be used in SNMP pull.
import VendorSNMP

def run(nodeList, gathDir, lineCnt, configData):

    hostName = ""                           # host name of node
    monIP = ""                              # monitoring IP
    realIP = ""				# real IP
    vendor = ""				# vendor name	
    snmp = ""				# snmp code
    string = ""    		 		# snmp string
    monName = ""				# UID for monitoring element	

    count = 0


    # set elements in node list to separte variables
    for node in nodeList:
        hostName = node[0]
        monIP = node[1]
        realIP = node[2]
        vendor = node[3]
        snmp = node[4]
        string = node[5]
        monName = node[6]	
        
        # run VendorSNMP
        if 'bad' not in string:
            VendorSNMP.run(gathDir, monName, hostName, monIP, realIP, string, vendor, snmp, configData)

        # increment and display progress
        count = count + 1
        print (str(count) + ' of ' + str(lineCnt))


