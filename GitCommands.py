# This module runs git commands to updated generated folder after pull

import subprocess
import datetime

def run():

    # Get current date
    timestamp = datetime.datetime.now()
    timestamp = str(timestamp.strftime('%Y-%m-%d') )
    
    # Run Git commands to upload previous
    p = subprocess.Popen(['git', 'add', '*'], cwd = "/home/mcabe/Obsidian", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)
    p = subprocess.Popen(['git', 'commit', '-m', timestamp], cwd = "/home/mcabe/Obsidian", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)
    p = subprocess.Popen(['git', 'push'], cwd = "/home/mcabe/Obsidian", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)
