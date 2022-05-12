# This module runs git commands to updated generated folder after polling SNMP

import subprocess
import datetime

def run():

    # Get current date
    timestamp = datetime.datetime.now()
    timestamp = str(timestamp.strftime('%Y-%m-%d'))
    
    # Run Git commands to upload previous
    # Run git add, though there should not be any changes
    p = subprocess.Popen(['git', 'add', '*'], cwd = "/home/mcabe/Obsidian", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)
    
    #Run git commit with time current date as timestamp
    p = subprocess.Popen(['git', 'commit', '-m', timestamp], cwd = "/home/mcabe/Obsidian", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)
    
    # Run git push to update file in Github
    p = subprocess.Popen(['git', 'push'], cwd = "/home/mcabe/Obsidian", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)
