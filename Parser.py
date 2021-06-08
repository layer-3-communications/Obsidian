# Module with different parsing methods

import re

# parser for single SNMP output
def general(output):
    output = re.sub(r'.*STRING:', '', output)
    output = output.replace('\"', '')
    output = output.replace('\\n', '')
    output = output.replace('\'', '')
    output = output.strip()
    return output

# parser for multiple SNMP output
def multiple(output):
    output = re.sub(r'.*STRING:', '', output)
    output = output.replace('\"', '')
    output = output.replace('\\n', ':')
    output = output.replace(' ', '')
    output = output.replace('\'', '')
    output = output.replace('\n', '')
    output = output.strip()
    return output


