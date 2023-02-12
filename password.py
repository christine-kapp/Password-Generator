# Password Random Character Generator

import  random

lowercase = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
specialchars = "!$"

valid_chars = lowercase+capital+numbers+specialchars

def genpassword(n):

    password = ""
    
    for i in range(n):
        
        selection = random.choice(valid_chars)
        password += selection 

    return password

length = int(input("Enter chosen password length: "))
password = genpassword(length)

print("Your generated password is: ",password)
