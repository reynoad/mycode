#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode 
configfile = open('vlanconfig.cfg', 'r')

## display file to the screen - .read() 
print(configfile.read())

## close file 
configfile.close()

