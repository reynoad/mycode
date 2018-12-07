#!/usr/bin/env python3

file = open('Hunter_Wife.txt', 'r')
print( 'File Name:', file.name )
print( 'File Open Mode:', file.mode )

text = file.readlines()

print("\t"+"\t".join(text))