'''
Created on 10-Mar-2024

@author: prashanth
'''
import sys
a=2 #int # hard-coded values
b=3.5 #float
c=6+8j #complex
d="dogs" #string
e=True #boolean
f=False #boolean
g=None #none 
print(type(a))
print(sys.getsizeof(a))
print(type(b))
print(sys.getsizeof(b))
print(type(c))
print(sys.getsizeof(c))
print(type(d))
print(sys.getsizeof(d))
print("e=", type(e))
print(sys.getsizeof(e))
print("f=", (f))
print(sys.getsizeof(f))
print("g", type(g))
print(sys.getsizeof(g))