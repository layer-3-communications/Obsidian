# main driver module
import NodeInfo
import VendorSNMP
import UpdateDB
import GatherInfo
import Date
import Directory 


def run(dbPath, hostGrp, configData):
    # get node infromation needed
    nodeList = NodeInfo.db(dbPath, hostGrp)

    # get count for progress
    lineCnt = len(nodeList)

    # generate system date
    date = Date.generate()

    # format directory name for generated files
    gathDir = "/home/mcabe/Obsidian/gather-outputs/%s-%s" % (hostGrp, date)

    # create directory name for files
    Directory.create(gathDir)

    # operations to be perform
    # gather information
    GatherInfo.run(nodeList, gathDir, lineCnt, configData)
    
    # take invertory.txt and updates database
    UpdateDB.run(gathDir, dbPath, hostGrp)

