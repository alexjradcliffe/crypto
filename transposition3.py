import math
import itertools



def putingrid():
    #ENTER MESSAGE HERE
    message = ""
    message = ''.join(message.split())
    #for keylen in range(2, len(message)):
    for keylen in range(2, 6):
        print("KEYLEN: " + str(keylen))
        array = [[0]*math.ceil((len(message)/keylen)) for i in range(keylen)]
        for x in range(0, len(array)):
            count = x
            for y in range(0, len(array[x])):
                try:
                    array[x][y]=message[count]
                except:
                    message = message + "X"
                    array[x][y]=message[count]
                    
                print(message[count])
                print(count)
                count+=keylen
        printans(keylen, array)



def printans(keylen, array):
    string = ""
    test = (list(itertools.permutations(array, keylen)))
    for a in range(0, len(test)):
        string = ""
        for z in range(0, len(test[a][0])):
            #string = string + test[2][0][z] + test[2][1][z] + test[2][2][z]
            #string = string + test[a][len(test[a])][z]
            for p in range(0, len(test[a])):
                string = string + test[a][p][z]
        print("KEYLEN: " + str(keylen))
        print(string)


putingrid()

    





            
                       
                    


