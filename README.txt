Intructions:

The config.yaml file hold the sqlite database file path, the group (database table) that will used in the scripts,
and the OIDS that are use in the SNMP pull for information. This file will need to be modify if a different group
needs to be run, OIDs changes, or database path changes.

Run python command on either executeAll.py, executeGenerate.py, or executeInfoGather.py file. The file executeAll.py
will run executeInfoGather.py first and then executeGenerate.py right after. The gather-output directory will contain
the csv generated from the infomation gather. This infomation would be updated in the database. The generate directory
contains all the generated configuations. They are sorted by group-date directory and each file is has the separate 
configs for each system.
