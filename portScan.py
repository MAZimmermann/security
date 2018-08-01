# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 17:15:27 2018

@author: MAZimmermann
"""

import socket as sk

for port in range(1, 1024):
    try:
        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        s.settimeout(1000)
        s.connect(('127.0.0.1', port))
        print('%d:***OPEN***'%port)
        s.close
    except: print('%d:CLOSED'%port)
