# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 21:04:43 2018

@author: MAZimmermann
"""

# Provides data endcoding and decoding
import base64

file1 = open("pwd.txt", "r")
file2 = open("b64pwd.txt", "wb")

for line in file1:
    clear = "administrator: " + str.strip(line) + "\n"
    new = clear.encode('ascii')
    file2.write(new)