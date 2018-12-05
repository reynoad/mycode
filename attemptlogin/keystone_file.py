#!/usr/bin/env python3

loginfail = 0
login = 0
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')
keystone_file_lines=keystone_file.readlines()
for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
    elif "-] Authorization failed" in keystone_file_lines[i]:
        login += 1
print('The number of failed log in attempts is ' + str(loginfail))
print('The number of successful log in attempts is ' + str(login))