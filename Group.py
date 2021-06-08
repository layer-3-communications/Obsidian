# gets host group and alias
def getData(c, hostGroup):

    # private variables
    groupAlias = ''
    dbQuary = "SELECT monGrpName FROM '%s'" % hostGroup

    # host group information from csv mapping to variables
    for row in c.execute(dbQuary):
        groupAlias = row[0]

    # return group information
    return groupAlias

# generate group config
def generateConfig(hostGroup, groupAlias, genDir):
    
    groupConfigFile = genDir + "/groupOutput-%s.txt" % (hostGroup)

    # open file to write group config
    groupConfig= open(groupConfigFile, "w")
   
    # contanct list
    contactList = ''

    # parse information for contacts
    contactOutput = "define hostgroup {" + \
                "\n\thostgroup_name\t\t%s" %hostGroup + \
                "\n\talias\t\t\t%s" %groupAlias + \
                "\n\tnotes\t\t\t\\nContact List (In order)\\n--------------------------------------------------------------------\\n" + contactList + "\\n--------------------------------------------------------------------\\n" + \
                "\n\tnotes_url\t\thttps,//ssl.layer3com.com" + \
                "\n}\n" + \
                "define servicegroup {" + \
                "\n\tservicegroup_name\t%s" %hostGroup + \
                "\n\talias\t\t\t%s" %groupAlias + \
                "\n\tnotes\t\t\t\\nContact List (In order)\\n--------------------------------------------------------------------\\n" + contactList + "\\n--------------------------------------------------------------------\\n" + \
                "\n\tnotes_url\t\thttps,//ssl.layer3com.com" + \
                "\n}\n"

    groupConfig.write(contactOutput)
    groupConfig.close()
