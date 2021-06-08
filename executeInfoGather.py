# main driver module
import FileYAML
import InfoGather

def run():
        # initiate data and configuration to be used
       	# obtain OID data from YAML file
	configData = FileYAML.loadConfig()
	dbPath, groupList = FileYAML.readParam(configData)


	for hostGrp in groupList:
		InfoGather.run(dbPath, hostGrp, configData)
run()
