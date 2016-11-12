from __future__ import print_function
from __future__ import division
import sys
import operator

python3 = True if sys.version_info.major > 2 else False
stdfreq = {
    "A" : 0.0817,
    "B" : 0.0149,
    "C" : 0.0278,
    "D" : 0.0425,
    "E" : 0.1270,
    "F" : 0.0223,
    "G" : 0.0202,
    "H" : 0.0609,
    "I" : 0.0697,
    "J" : 0.0015,
    "K" : 0.0077,
    "L" : 0.0403,
    "M" : 0.0241,
    "N" : 0.0675,
    "O" : 0.0751,
    "P" : 0.0193,
    "Q" : 0.0010,
    "R" : 0.0599,
    "S" : 0.0633,
    "T" : 0.0906,
    "U" : 0.0276,
    "V" : 0.0098,
    "W" : 0.0236,
    "X" : 0.0015,
    "Y" : 0.0197,
    "Z" : 0.0007,
}

def freq2occ(freq, l):
    occ = {}
    for i in freq:
        occ[i] = freq[i] * l
    return occ

def occurences(string):
    string = string.upper()
    occ = {chr(i) : 0 for i in range(65, 91)}
    for i in string:
        if i in occ:
            occ[i] += 1
    return occ

def frequency(string):
    N = len(string)
    occ = occurences(string)
    freq = {chr(i) : 0 for i in range(65, 91)}
    for i in occ:
        freq[i] = round(float(occ[i]) / N, 3)
    return(freq)

def sortedfreq(string):
    freq = frequency(string)
    sortedf = sorted(freq.items(), key=operator.itemgetter(1), reverse=1)
    return sortedf

def chi_sq(occC, l):
    occE = freq2occ(stdfreq, l)
    chi_sq = 0
    for i in range(65, 91):
        chi_sq += ((occC[chr(i)] - occE[chr(i)]) ** 2) / occE[chr(i)]
    return chi_sq

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

msg = input("Message: ") if python3 else raw_input("Message: ")
x = chi_sq(occurences(msg.upper()), len(msg))
opta = 1
optb = 0

for i in range(26):
    e = sortedfreq(msg)[i][0]
    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        b = (ord(e) - 65 - 4 * a) % 26
        if chi_sq((occurences(decode(msg, a, b))), len(msg)) < x:
            opta = a
            optb = b
            x = chi_sq(occurences(decode(msg, a, b)), len(msg))

print(decode(msg, opta, optb))
