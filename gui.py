#!/usr/bin/env python

import urllib2
import sys
from pythonzenity import Password, Message
def main():
    password = 'lincoder'
    user_input = Password(text="Enter Your Password!!")
    if user_input !=password:
        sys.exit('Incorrect Password \n')
if __name__ == "__main__" :
    main()
lincoder=Message(text="Password Verified successfully!!")
print (lincoder)
print ("Checking Your Public Ip Address... \n")
print ("Your Public Ip is :")
print(urllib2.urlopen('http://icanhazip.com').read())
