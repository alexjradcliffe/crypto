from __future__ import print_function
from __future__ import division
from analyse import *
import sys

python3 = True if sys.version_info.major > 2 else False




def encKey(a, b):
    '''Produces the encoding key with a shift of n.
    '''
    key = {}
    for i in range(26):
        key[chr(i + 97)] = chr((a * i + b) % 26 + 65)
    return key

def decKey(a, b):
    '''Produces the decoding key with a shift of n.
    '''
    key = {}
    for i in range(26):
        key[chr((a * i + b) % 26 + 65)] = chr(i + 97)
    return key

def encode(msg, a, b):
    '''Encodes the message.
    '''
    msg = msg.lower()
    enc = ""
    key = encKey(a, b)
    for l in msg:
        if l in key:
            enc += key[l]
    return(enc)

def decode(msg, a, b):
    '''Decodes the message.
    '''
    msg = msg.upper()
    dec = ""
    key = decKey(a, b)
    for l in msg:
        if l in key:
            dec += key[l]
    return(dec)
     
while terminate == False:
    command = input("Command: ") if python3 else raw_input("Command: ")
    if command == 'Q':
        terminate = True
    else:
        msg = input("Message: ") if python3 else raw_input("Message: ")
        print("x -> ax + b")
        a = int(input("a: ")) if python3 else int(raw_input("a: "))
        b = int(input("b: ")) if python3 else int(raw_input("b: "))
        if command == 'E':
            print(encode(msg, a, b))
        if command == 'D':
            print(decode(msg, a, b))

