# main driver module
import FileYAML
import GenerateConfig

def run():
        # initiate data and configuration to be used
       	# obtain OID data from YAML file
	configData = FileYAML.loadConfig()
	dbPath, groupList = FileYAML.readParam(configData)

	for hostGrp in groupList:
		# generate configuration with updated database
		GenerateConfig.run(dbPath, hostGrp)

run()
