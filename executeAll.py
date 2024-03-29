# main driver module
#driver module to run both InfoGather and GenerateConfig

import FileYAML
import GenerateConfig
import InfoGather
import GitCommands

def run():
    # initiate data and configuration to be used
    # obtain OID data from YAML file
    configData = FileYAML.loadConfig()
    dbPath, groupList = FileYAML.readParam(configData)

    for hostGrp in groupList:
        # gather informaiton and update database
        InfoGather.run(dbPath, hostGrp, configData)	

        # generate configuration with updated database
        GenerateConfig.run(dbPath, hostGrp)

        # Run Git commands to upload files to Github
        GitCommands.run()
run()
