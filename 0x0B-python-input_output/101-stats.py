#!/usr/bin/python3
"""Module 101-stats.py
write a script that reads stdin,
line by line and computes metrics:
"""

import sys

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    print(f'Processing Message from sys.stdin *****{line}*****')
print("Done")

