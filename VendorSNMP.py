# This module obtains and parses informtaion form SNMP pulls. Calls RecordOutputs
# to record either failled or success.

import SimpleMessage
import RecordOutput
import Parser
import FileYAML

def run(gathDir, monName, hostName, monIP, realIP, string, vendor, snmp, configData):
    # private variables
    modOID = ''
    verOID = ''
    serOID = ''
    count = 0
    findStr = "STRING"
    
    # obtain OID per snmp type
    modOID, verOID, serOID = FileYAML.getOID(snmp, configData)

    # obtain version SNMP and parses the output
    output = SimpleMessage.run(string, monIP, verOID)
    if findStr in output: 
            version = Parser.general(output)
    else:
            version = "NI!"

    # obtain model SNMP and parses the output
    output = SimpleMessage.run(string, monIP, modOID)
    if findStr in output: 
            model = Parser.general(output)
    else:
            model = "NI!"

    # obtain serials SNMP and parses the output
    output = SimpleMessage.run(string, monIP, serOID)
    if findStr in output: 
            serial = Parser.multiple(output)
            for i in serial:
                    if i == ':':
                            count = count + 1
            numDevices = count
    else:
            serial = "NI!"

    # record output based on success or fail
    if 'NI!' not in version:
            if 'NI!' not in model:
                    if 'NI!' not in serial:
                            RecordOutput.success(gathDir, monName, hostName, monIP, realIP, vendor, model, version, serial, numDevices)
    else:	
            RecordOutput.fail(gathDir, monName, hostName, monIP, realIP, vendor)




