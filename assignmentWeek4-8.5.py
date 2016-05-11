'''
Count number of lines starting withe 'From' in a text
Created on May 5, 2016
@author: course
@author: dinh
'''

filename = raw_input('Enter file name: ')
if len(filename) < 1:
    filename = 'mbox-short.txt'

filehandle = open(filename)
count = 0
for line in filehandle:
    line = line.strip()
    l = line.split()
    if len(l) > 0 and l[0] == 'From':
        print l[1]
        count = count + 1
print 'There were', count, 'lines in the file with From as the first word'