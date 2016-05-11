'''
Print all lines in file in uppercase
Created on May 4, 2016
@author: course
@author: dinh
'''

filename = raw_input('Enter file name: ')
try:
    filehandle = open(filename)
except:
    print 'Can not open', filename
    exit()
for line in filehandle:
    line = line.rstrip()
    print line.upper()
filehandle.close()