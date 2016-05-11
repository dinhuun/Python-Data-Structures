'''
Count, sort and print numbers of appearances of words in a text
Created on May 5, 2016
@author: course
@author: dinh
'''

filename = raw_input('Enter file name: ')
filehandle = open(filename)
l = list()
for line in filehandle:
    line = line.strip()
    words = line.split()
    for w in words:
        if w not in l:
            l.append(w)
filehandle.close()
s = sorted(l)
print s