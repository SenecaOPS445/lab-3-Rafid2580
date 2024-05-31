#!/usr/bin/env python3
# Author ID: 186140216

import os

def free_space():
    stream = os.popen("df -h | grep '/$' | awk '{print $4}'")
    output = stream.read()
    return output.strip()

if __name__ == '__main__':
    print(free_space())

