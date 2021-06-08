from string import Template

# gets host group and alias
def generateConfig(c, hostGroup, genDir):

	# database quary
	dbQuary = "SELECT monName, hostName, realIP, monIP, parents, remInt, remIntNote, locInt, locIntNote, manuf, numDevices, model, softVer, serials, playbook FROM %s ORDER BY monName" % hostGroup

	nagiosConfigFile = genDir + "/%s.cfg" % hostGroup

	nagiosConfig = open(nagiosConfigFile, "w")

	# private variable

	# host group information from csv mapping to variables
	for row in c.execute(dbQuary):
            monName = row[0]
            hostName = row[1]
            realIP = row[2]
            monIP = row[3]
            parents = row[4]
            rInt = row[5]
            rIntNotes = row[6]
            lInt = row[7]
            lIntNotes = row[8]
            manuf = row[9]
            numDevices = row[10]
            deviceType = row[11]
            version = row[12]
            serialNums = row[13]
            playbook = row[14]

            # runs each parsing methods before writing data to file
            parents = parseParents(parents, hostGroup)
            
            if serialNums is not None:
                serialNote = parseSerials(serialNums)   
            else:
                serialNote = ''
            
            if playbook is None:
                playbook = ''

            notes = parseNotes(hostName, realIP, numDevices, manuf, deviceType, rInt, rIntNotes, lInt, lIntNotes, version, serialNote, playbook)
            nagiosOutput = generateNagiosConfig(hostGroup, monName, parents, hostName, monIP, notes)
            nagiosConfig.write(nagiosOutput)

            monName = ''
            hostName = ''
            realIP = ''
            monIP = ''
            parent1 = ''
            parent2 = ''
            rInt = ''
            rIntNotes = ''
            lInt = ''
            lIntNotes = ''
            manuf = ''
            numDevices = ''
            deviceType = ''
            version = ''
            serialNums = ''
            serialNote = ''
            playbook = ''

	# close file
	nagiosConfig.close()

# parse notes
def parseNotes(hostName,realIP, numDevices, manuf, deviceType, rInt, rIntNotes, lInt, lIntNotes, version, serialNote, playbook):
	notes = "\\n Customer Host Name: %s" % hostName +\
		"\\n Real IP: %s" % realIP +\
		"\\n Device: %s %s %s" % (numDevices,  manuf, deviceType) +\
		"\\n Parent interface: %s(%s), Local Interface: %s(%s)" %( rInt, rIntNotes, lInt, lIntNotes) + \
		"\\n Version: %s" % version + \
		"\\n Serials: %s" % serialNote + \
		"\\n Playbook: %s\\n" % playbook

	return notes

# condition to handle more than one parent
def parseParents(parents, hostGroup):
    
    if parents is None:
            parents = ''
    else:
            parents = parents.replace(':', ',')


    return parents


# combines all serials to on string
def parseSerials(serialNums):
	# condition to handle serial number
	serialNote = ''
	serialNums = serialNums.replace(':', ', ')
	serialNote = serialNote + serialNums
	return serialNote


# generate the Nagios configurations based off templates 
def generateNagiosConfig(hostGroup, monName, parents, hostName, monIP, notes):

	
	if parents is '':
		with open('/home/mcabe/Obsidian/templates/nagios-noParent.txt', 'r') as templateFile:
			nagiosOutput = Template(templateFile.read())  
		
		parse ={  'hostGroup':hostGroup, 'monName':monName, 'hostName':hostName, 'monIP':monIP, 'notes':notes }
		nagiosOutput = nagiosOutput.substitute(parse)
	
	else:
                with open('/home/mcabe/Obsidian/templates/nagios.txt', 'r') as templateFile:
                        nagiosOutput = Template(templateFile.read())
                        
                parse ={  'hostGroup':hostGroup, 'monName':monName, 'parents':parents, 'hostName':hostName, 'monIP':monIP, 'notes':notes }
                nagiosOutput = nagiosOutput.substitute(parse)

	return nagiosOutput



