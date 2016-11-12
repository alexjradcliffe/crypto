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



def frequency(string):
    N = len(string)
    freq = {}
    occ = occurences(string)
    for i in occ:
        freq[i] = round(float(occ[i]) / N, 3)
    return(freq)
        

def sortedfreq(string):
    freq = frequency(string)
    sortedf = sorted(freq.items(), key=operator.itemgetter(1), reverse=1)
    return sortedf
        
        
for i in sortedfreq(msg):
    print i
