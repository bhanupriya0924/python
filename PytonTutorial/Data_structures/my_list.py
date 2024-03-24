'''
Created on 22-Mar-2024

@author: prashanth
'''
from itertools import count
'''
a=[]
print("a", type(a))
print(a)#list
a1=[1,2, 3, "bhanu", 2.3, True]
print("a1",(a1))
b=()
print("b", type(b))
print(b)

'''
'''
c=[1, 2, 3, 4]
c=list(range(2, 12, 13))
c.sort()
print(c)
print("c->", c)
d=[1, 2, 3, 4]
c.append(d)
c.append(56)
print("after appending", c)
c.extend(d)
print("after extending d")
print(c)
#c.clear()
#print(c)
e=c.copy()
print("e=", e)
print(c.index(1))
c.insert(9, 100)
print(c)

print(c.pop(4))
print(c)

c.remove(56)
print(c)
c.reverse()
print(c)

c.count(2)
print(c)
print(len(c))
'''
'''
a=[1, 2, 2, 3, 4, 6, 5, 6, 6]
b=a.copy()
for i in b:
    ele_count=b.count(i)
    print(f"{i}--> {ele_count}times")
for j in range(ele_count):
    b.remove(i)
print(a)
'''
a=[1, 2, 2, 3, 4, 6, 5, 6, 6]
b=a.copy()
i=0
while True:
    element=b[i]
    ele_count=b.count(element)
    print(f"{element}-->{ele_count} times")
    for j in range(ele_count):
      b.remove(element) 
    if (len(b)==0):
     break

