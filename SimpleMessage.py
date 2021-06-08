# This module takes all pass in variables and creates a SNMP pull and returns the output. 
# If unable to connect, the FAIL TO CONNECT will be return instead

import subprocess
import re

def run(string, ipAddr, oid):
   
    data = ""

    #run ssh comamand
    p = subprocess.Popen(['snmpwalk', '-v', '2c', '-c', string,  ipAddr, oid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    data = str(out)

    data = data.replace('b\'', '')
    data = re.sub(r'iso', '\n', data)

    return data

