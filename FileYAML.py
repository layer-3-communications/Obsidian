# This module obtains data via YAML files

import yaml

# load YAMl config file to object
def loadConfig():

	yamlFile = '/home/mcabe/Obsidian/config.yml'

	with open(yamlFile, 'r') as yamlData:
		configData = yaml.load(yamlData)

	return configData

# pulls OID data from yaml object base on snmp code
def getOID(snmp, configData):
	oidTpye = configData.get(snmp)
	modOID = oidTpye['model']
	verOID = oidTpye['version']
	serOID = oidTpye['serials']

	return modOID, verOID, serOID

# pull parameter data for running the script
def readParam(configData):
	configParam = configData.get('config')
	dbPath = configParam['dbPath']
	hostGrp = configParam['hostGrp']

	return dbPath, hostGrp

