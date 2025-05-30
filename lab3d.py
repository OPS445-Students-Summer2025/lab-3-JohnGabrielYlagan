#!/usr/bin/env python3

'''Lab 3 - Linux commands and builtin functions in os'''
# Author ID: jgylagan

import os
import subprocess
'''
os.popen('ls')
os.popen('whoami')
os.popen('ifconfig')
def list_directory():
    os.system('ls')

# Main Program
if __name__ == '__main__':
    list_directory()
'''

def free_space():
    myoutput = os.popen("df -h | grep '/$' | awk '{print $4}'")
    myresult = myoutput.read()
    return myresult.strip()
   # grep and awk used to look for specific info of my vm


# Main Program
if __name__ == '__main__':
    print(free_space())