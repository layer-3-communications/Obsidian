# This module runs git commands to updated generated folder after pull

import subprocess

def run():
    #run ssh comamand
    p = subprocess.Popen(['git', 'add', '*'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)
    print (out)
    p = subprocess.Popen(['git', 'commit', '-m', '/"updated generated/"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)
    print (out)
    p = subprocess.Popen(['git', 'push'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    data = str(out)
    print (out)

run()
