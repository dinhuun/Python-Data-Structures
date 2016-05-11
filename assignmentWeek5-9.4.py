'''
Count appearances of email senders in a text and print the most frequent sender and the number of emails
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
        sender = words[1]
        counts[sender] = counts.get(sender,0) + 1
max = 0
maxsender = None
for sender,count in counts.items():
    if count > max:
        max = count
        maxsender = sender
print maxsender, max