# This module runs git commands to updated generated folder after pull

import subprocess
import datetime

def run():

    # Get current date
    timestamp = datetime.datetime.now()
    timestamp = str(timestamp.strftime('%Y-%m-%d') )
    
    # Run Git commands to upload previous run probe with time stamp
    p = subprocess.Popen(['git', 'add', '*'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)
    p = subprocess.Popen(['git', 'commit', '-m', timestamp], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)
    p = subprocess.Popen(['git', 'push'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)

run()
