from __future__ import print_function
from __future__ import division
import sys

python3 = True if sys.version_info.major > 2 else False
terminate = False


def encKey(n):
    '''Produces the encoding key with a shift of n.
    '''
    key = {}
    for i in range(26):
        key[chr(i + 97)] = chr((i + n) % 26 + 65)
    return key

def decKey(n):
    '''Produces the decoding key with a shift of n.
    '''
    key = {}
    for i in range(26):
        key[chr(i + 65)] = chr((i - n) % 26 + 97)
    return key

def encode(msg, n):
    '''Encodes the message.
    '''
    msg = msg.lower()
    enc = ""
    key = encKey(n)
    for l in msg:
        if l in key:
            enc += key[l]
    return(enc)

def decode(msg, n):
    '''Decodes the message.
    '''
    msg = msg.upper()
    dec = ""
    key = decKey(n)
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
        cue = ("Number of characters to be shifted"
               + "(a encrypted as E would be 4.) ")
        n = input(cue) if python3 else raw_input(cue)
        n = int(n)
        if command == 'E':
            print(encode(msg, n))
        if command == 'D':
            print(decode(msg, n))
    

        


