#!/usr/bin/env python3

print ('What is the hostname? ')
hostname = str(input())
if hostname == 'mtg' or 'MTG' or 'mTg' or 'MTg' or 'mTG' or 'MtG':
	print('The hostname was found to be ' + hostname)