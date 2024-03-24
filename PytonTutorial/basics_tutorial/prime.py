'''
Created on 19-Mar-2024

@author: prashanth
'''

a=int(input("enter a number"))
if a==1:
    print(" prime number")
for i in range(2, a+1):
    b=a%i
    if b==0 and i<a:
        print("not a prime number")
        break
if b==0 and i==a:
    print("it is prime")
    