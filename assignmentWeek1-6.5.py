'''
Locate floating number in short text
Created on May 4, 2016
@author: course
@author: dinh
'''

text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('.')
n = text[pos-1:pos+5]
print float(n)