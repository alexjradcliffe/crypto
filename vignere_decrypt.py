from __future__ import print_function
from __future__ import division
import sys
import string

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
} #Letters of the alphabet with frequencies in English

def freq2occ(freq, l):
    '''
Takes the frequency distribution and produces the expected occurences.
freq = frequency distribution (dict)
l = length of text (int)
'''
    occ = {}
    for i in freq:
        occ[i] = freq[i] * l
    return occ

def occurences(string):
    """
    Returns a dict of the no. of occurences of each letter in the string
    """
    string = string.upper()
    occ = {chr(i) : 0 for i in range(65, 91)}
    for i in string:
        if i in occ:
            occ[i] += 1
    return occ

def frequency(string):
    """
    Returns the frequency of each letter in the string
    """
    N = len(string)
    occ = occurences(string)
    freq = {chr(i) : 0 for i in range(65, 91)}
    for i in occ:
        freq[i] = round(float(occ[i]) / N, 3)
    return(freq)
        
def chi_sq(occC, l):
    """
    Returns the results of a chi-squared test between the decrypted ciphertext and the standard frequencies
    """
    occE = freq2occ(stdfreq, l) # Expectation values for occurences of each letter in a text of a particular length
    chi_sq = 0
    for i in range(65, 91):
        chi_sq += ((occC[chr(i)] - occE[chr(i)]) ** 2) / occE[chr(i)]
    return chi_sq


def decKey(n):
    """
    Produces the decoding key with a shift of n.
    """
    key = {}
    for i in range(26):
        key[chr(i + 65)] = chr((i - n) % 26 + 97)
    return key

def decode(msg, n):
    """
    Decodes the message with a shift of n.
    "
    msg = msg.upper()
    dec = ""
    key = decKey(n)
    for l in msg:
        if l in key:
            dec += key[l]
    return(dec)


if __name__ == '__main__':
    msg = input("Message: ") if python3 else raw_input("Message: ")
    keylen = input("Key length: ") if python3 else raw_input("Key length: ")
    keylen = int(keylen)
    
if __name__ == '__main__':
    msg = msg.upper()
    newMsg = ""
    for i in range(len(msg)):
        if ord(msg[i]) > 64 and ord(msg[i]) < 91:
            newMsg += msg[i]
    msg = newMsg


def columns(msg, l):
    columns = ["" for i in range(l)]
    for i in range(len(msg)):
        columns[i % l] += msg[i]
    return columns

if __name__ == '__main__':
    msgcols = columns(msg, keylen)
    newcols = ["" for i in range(keylen)]
    for j in range(keylen): #column is msgcols[j]
        x = chi_sq(occurences(msgcols[j].upper()), keylen)
        n = [0 for i in range(keylen)]
        for i in range(1, 26):
            if chi_sq((occurences(decode(msgcols[j], i))), keylen) < x:
                n[j] = i
                x = chi_sq(occurences(decode(msgcols[j], i)), keylen)
        newcols[j] = decode(msgcols[j], n[j])

    decoded = ""

    for j in range(len(newcols[-1])): #column length
        for i in range(keylen): #row
            try:
                decoded += newcols[i][j]
            except IndexError:
                break
    print(decoded)





