import operator
import sys



if len(sys.argv) >= 2:
    msg = sys.argv[1]
else:
    msg = raw_input("Enter message: ")


def occurences(string):
    occ = {}
    for i in string:
        if i in occ:
            occ[i] += 1
        else:
            occ[i] = 1
    return occ


def ioc(string):
    N = len(string)
    total = 0
    occ = occurences(string)
    for i in occ:
        total += occ[i] * ( occ[i] - 1 )
    return float(total) / (N * (N - 1))
        
        
print ioc(msg)
