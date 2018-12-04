#!/usr/bin/env python3

#Import shell utilities
import shutil
import os

#Using the os module and the chdir method
os.chdir('/home/student/mycode/')

#Using shutil and move
shutil.move('raynor.obj', 'ceph_storage/')

#Prompt the user for a new name
xname = input('What is the new name for kerrigan.obj? ')

#Move the kerrigan.obj
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)