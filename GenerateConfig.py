import Group
import Database
import Nagios
import SRX
import Grafana
import Directory
import Date
import Oxidized
import Inventory

def run(databasePath, hostGroup):

    # generate system date
    date = Date.generate()

    # format directory name for generated files
    genDir = "/home/mcabe/Obsidian/generated/%s-%s" % (hostGroup, date)

    # create directory name for files
    Directory.create(genDir)

    # establis database connecction and returns it
    conn = Database.connect(databasePath)

    # gather information for group configuration
    groupAlias = Group.getData(conn, hostGroup)

    # generate group config
    Group.generateConfig(hostGroup, groupAlias, genDir)
    
    # gather information and generate Nagios configuation
    Nagios.generateConfig(conn, hostGroup, genDir)

    # gather information and generate SRX configuration
    SRX.generateConfig(conn, hostGroup, genDir)

    # gather information and generate SRX configuration
    Grafana.generateConfig(conn, hostGroup, genDir)

    # gather information and generate SRX configuration
    Oxidized.generateConfig(conn, hostGroup, genDir)

    Inventory.generateInventory(conn, hostGroup, genDir)

    # close database connection
    conn.close()

