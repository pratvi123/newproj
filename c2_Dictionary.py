# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 17:51:47 2017

@author: KAZI
"""
D={}# Empty Dictionary
print(type(D))# print data type for D
D['name']='KAZI'
D['Place']='Bangalore'
D['numb']=560039

print(D['name']) # accessing the value for key 'name'
D['Coountry']='INDIA'
D['states']=['karnataka' ,'maharashtra']
print(D) # print contents of D


# clearing the content of D1
D1={'name':'real','place':'bangalore'}
#print(D1)
#D1.clear()
#print(D1)


D1_copy=D1.copy();
D1_copy2=D1
del D1['name']
print(D1)


L=['name','place','area']
D3={}
D3=D3.fromkeys(L,0)

print(D.get('name'))
print(D.items())

for i in D.iteritems():
    print i
for i in D.iterkeys():
    print i
for i in D.itervalues():
    print i
print(D.keys())

print(D.pop('name'))
print(D.popitem())

D4={'numb':25}
print(D4.update({'name':'kazi'}))
    
    
