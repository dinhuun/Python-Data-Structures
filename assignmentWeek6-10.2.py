'''
Created on May 5, 2016
@author: course
@author: dinh
'''

name = raw_input('Enter file: ')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)

counts = dict()
for line in handle:
    line = line.strip()
    words = line.split()
    if len(words) > 0 and words[0] == 'From':
        pos = line.find(':')
        hour = line[pos - 2: pos]
        counts[hour] = counts.get(hour,0) + 1
for hour in sorted(counts):
    print hour,counts[hour]