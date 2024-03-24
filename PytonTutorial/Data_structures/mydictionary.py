'''
Created on 23-Mar-2024

@author: prashanth
'''
d={1:"bhanu", 2:"shashikala", 3:"sarvani", 4:"sumanth"}
c={1, 2, 3, 4}
print(d)
print(d[1])
d[2]="shashi"
print(d)
print(d.fromkeys(c, "value"))
print(d.items())
print(d.keys())
print(d.values())