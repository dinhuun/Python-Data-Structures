'''
Find, accumulate, and average spam confidences in lines starting with 'X-DSPAM-Confidence' in a text
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
c = 0
s = 0
for line in filehandle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    line = line.strip()
    pos = line.find('.')
    v = line[pos-1:]
    v = float(v)
    c = c + 1
    s = s + v
filehandle.close()
print 'Average spam confidence:', s/c