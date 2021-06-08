# This module will record results. Success will record all full outputs to a separte file per node.
# Fail will record node name and IP to a single file.

def fail(gathDir, monName, hostName, monIP, realIP, vendor):
    failFile = open(gathDir + '/failIP.txt', 'a')
    failFile.write('%s,%s,%s,%s,%s\n' % (hostName, monIP, realIP, vendor, monName))
    failFile.close()

def success(gathDir, monName, hostName, monIP, realIP, vendor, model, version, serial, numDevices):
    outputFile = open(gathDir + '/inventory.csv', 'a')
    outputFile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (hostName, monIP, realIP,vendor, model, version, serial, monName,numDevices))
    outputFile.close()


