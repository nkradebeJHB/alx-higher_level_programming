#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

with request.urlopen("https://intranet.hbtn.io/status") as response:
    res = response.read()
print('Body response:')
print('\t- type:', type(res))
print('\t- content:', res)
print('\t- utf8 content:', res.decode('utf8'))
