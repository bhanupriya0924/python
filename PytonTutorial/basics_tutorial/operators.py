'''
Created on 10-Mar-2024

@author: prashanth

1.operators :symbols which performs operation on one or more operands(variables)
2. Arithmetic operators :+, -, /, *, %, **, // 
3. Logical operators: AND, OR, NOT
4. Assignment operator:=
5. Relational comparison operators:>,<, <=, >=, ==, !=
6. Increment/Decrement: ++, --
7. Membership Operators:in, not in 
8. Identity Operators: is , is not 
'''
a=10
b=20 
c=a+b
print(c)
d= int(input("please enter a number:")) #type catsting
e=int(input("please enter a number:"))
f=d+e
'''print(f)
print(type(d))
print(type(e))
print(type(f))
print(True and True)
print(True and False)
print(False and False)

print (True or False)
print(False or False)
print(True or True)
print(not True)'''
print(5>8) #false
print(5>=8) #false
print(5<8) #True
print(5<=8)# True
print(5==8)#False
print(5!=8)# True

a=3
a=a+1
a+=1
a-=1
print(a)
print('a' in 'bhanu')
print('A'  not in 'bhanu')

a=2
b=2
print(a is b)
print(id(a)) #when id is equal same memory location and when id is different allocate anothor
print(id(b))