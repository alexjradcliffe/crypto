from __future__ import print_function
from __future__ import division
import operator
import sys

python3 = True if sys.version_info.major > 2 else False
if len(sys.argv) >= 2:
    msg = sys.argv[1]
else:
    msg = input("Enter message: ") if python3 else raw_input("Enter message: ")

class ciphertext:
    'Class for ciphertext'
    def __init__(self, inputMessage):
        self.inputMessage = inputMessage
        self.inputMessage = self.inputMessage.upper()
        newMsg = ""
        for i in range(len(self.inputMessage)):
            if (ord(self.inputMessage[i]) >= 65 and
                ord(self.inputMessage[i]) < 91):
                newMsg += self.inputMessage[i]
        self.inputMessage = newMsg
        
    def __str__(self):
        return self.inputMessage

    def __repr__(self): 
        return self.inputMessage

    def occurences(self):
        occ = {chr(i) : 0 for i in range(65, 91)}
        for i in self.inputMessage:
            if i in occ:
                occ[i] += 1
        return occ

    def nocc(self, n):
        occ = {}
        for i in range(len(self.inputMessage) + 1 - n):
            if self.inputMessage[i : i + n] in occ:
                occ[self.inputMessage[i : i + n]] += 1
            else:
                occ[self.inputMessage[i : i + n]] = 1
        return occ

    def frequency(self):
        N = len(self.inputMessage)
        occ = self.occurences()
        freq = {chr(i) : 0 for i in range(65, 91)}
        for i in occ:
            freq[i] = round(float(occ[i]) / N, 3)
        return(freq)


print(ciphertext("Hello!").occurences())
print(ciphertext("Hello!").nocc(2))
