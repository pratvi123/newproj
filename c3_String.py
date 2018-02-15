# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 17:49:34 2017

@author: KAZI
"""

S='Real Time Time Signals Technologies'
#S="Real Time Signals Technologies"
Para="""Real time Signals
Technologies"""
print(len(S))
print(len(Para))

print(S[0:4])

#S[3]='K'

print(S.upper())
print(S.lower())
print(S.title())
print(Para.capitalize())
print(S.split()) # returns a list with each word as element

S1='Real;Time;Signals;Technologies'
print(S1.split(';'))
print(S[S.find('Signals'):S.find('Signals')+len('Signals')])
print(S.count('Time'))

S2="\n\n\n\nReal Time Signals     "
print(S2.strip('\n')) 

print(S.endswith('Technologies'))
print(S.startswith('Real'))
print(S.isalnum())

S3='REAl'
print(S3.isalpha())

S4='real23'
print(S3.isalnum())
print(S3.islower())

S5='1234'
print(S5.isdigit())
print(S5.join('real '))
print('eral'+S5)
print(S5.replace('4','1'))
print(S5.split)

S="Real Time"
new_S=""
for letter in S:
    new_S=new_S+letter
print(new_S)

S6='Real Time Signals hgyt jhbgv hg'
vol=[]
non_vol=[]




      