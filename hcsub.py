from __future__ import print_function
from __future__ import division
import operator
import sys
import math
import random

# Uses a greedy random search algorithm to solve any substitution cipher

python3 = True if sys.version_info.major > 2 else False
if len(sys.argv) >= 2:
    msg = sys.argv[1]
else:
    msg = input("Enter message: ") if python3 else raw_input("Enter message: ")

msg = msg.upper()
newMsg = ""
for i in range(len(msg)):
    if ord(msg[i]) > 64 and ord(msg[i]) < 91:
        newMsg += msg[i]
msg = newMsg
# Sanitising the message
with open('english_quadgrams.txt') as f:
    lines = f.read().splitlines()

stdQuadOcc = {}
for line in lines:
    stdQuadOcc[line.split()[0]] = int(line.split()[1])

total = 0
for count in stdQuadOcc.values():
    total += count

def score(quad):
    # Gives the score for a quadgram (a measure of how likely it is to occur in standard English
    if quad in stdQuadOcc:
        score = math.log10(float(stdQuadOcc[quad]/total))
    else:
        score = math.log10(0.01/total)
    return score

def decode(msg, keystr):
    """
    Decodes the message.
    """
    keystr = keystr.upper()
    msg = msg.upper()
    dec = ""
    for l in msg:
        dec += chr(keystr.index(l) + 65)
    return(dec)

def fitness(msg, keystr):
    """
    Gives the fitness of a given keystr for a message
    """
    msg = decode(msg, keystr)
    fitness = 0
    for i in range(len(msg) - 3):
        fitness += score(msg[i : i + 4])
    return fitness

def randSwitch(keystr):
    """
    Switches a random pair of letters in the keystr
    """
    a = random.randint(0, 25)
    b = random.randint(0, 25)
    while a == b:
        b = random.randint(0, 25)
    if a > b:
        a, b = b, a
    keystr = (keystr[:a] + keystr[b] + keystr[a + 1:b]
              + keystr[a] + keystr[b + 1:])
    return keystr

def optimize(msg, keystr):
    """
    Will use a greedy random search to find the optimal keystr
    Returns the optimal keystr along with it's fitness
    """
    maxfit = fitness(msg, keystr)
    iterations = 0
    while iterations < 1000:
        newkey = randSwitch(keystr)
        if fitness(msg, newkey) > maxfit:
            keystr = newkey
            maxfit = fitness(msg, keystr)
            iterations = 0
        else:
            iterations += 1
    return [keystr, maxfit]



while True:
    # Loops infinitely in case it doesn't get it first time.
    k = optimize(msg, "YBXONGSWKCPZFMTDHRQUJVELIA") # Just a random keystr to start with
    print(k)
    print(decode(msg, k[0]).lower())

