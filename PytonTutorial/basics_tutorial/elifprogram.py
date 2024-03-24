'''
Created on 12-Mar-2024

@author: prashanth
'''
age=int(input("Enter the age"))
if age>18:
    print("You are an adult")
elif age >=13:
    print("You are a teenager")
else:
    print("You are a child")
    

if age>13:# nested if
    if age>18:
        print("You are an adult")
    else:
        print("You are a teenager")
        
else:
    print("You are a child")