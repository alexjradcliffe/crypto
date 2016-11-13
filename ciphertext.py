from __future__ import print_function
from __future__ import division
import operator
import sys
import random
import math

python3 = True if sys.version_info.major > 2 else False
if len(sys.argv) >= 2:
    msg = sys.argv[1]
else:
    msg = input("Enter message: ") if python3 else raw_input("Enter message: ")

with open('english_quadgrams.txt') as f:
    lines = f.read().splitlines()
stdQuadOcc = {}
for line in lines:
    stdQuadOcc[line.split()[0]] = int(line.split()[1])

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

    def __len__(self):
        return len(self.inputMessage)

    def occurences(self):
        occ = {chr(i) : 0 for i in range(65, 91)}
        for i in self.inputMessage:
            if i in occ:
                occ[i] += 1
        return occ

    def nocc(self, n):
        occ = {}
        for i in range(len(self) + 1 - n):
            if self.inputMessage[i : i + n] in occ:
                occ[self.inputMessage[i : i + n]] += 1
            else:
                occ[self.inputMessage[i : i + n]] = 1
        return occ

    def frequency(self):
        N = len(self)
        occ = self.occurences()
        freq = {chr(i) : 0 for i in range(65, 91)}
        for i in occ:
            freq[i] = round(float(occ[i]) / N, 3)
        return(freq)

    def nfreq(self, n):
        N = len(self) + 1 - n
        occ = self.nocc(n)
        freq = {}
        for i in occ:
            freq[i] = round(float(occ[i]) / N, 3)
        return(freq)

    def sortedfreq(self):
        freq = self.frequency()
        sortedf = sorted(freq.items(), key=operator.itemgetter(1), reverse=1)
        return sortedf


    def sortednfreq(self, n):
        freq = self.nfreq(n)
        sortedf = sorted(freq.items(), key=operator.itemgetter(1), reverse=1)
        return sortedf


    def ioc(self):
        N = len(self)
        total = 0
        occ = self.occurences()
        for i in occ:
            total += occ[i] * ( occ[i] - 1 )
        return float(total) / (N * (N - 1)) 


    def analyse(self):
        sf = self.sortedfreq()
        sbf = self.sortednfreq(2)
        stf = self.sortednfreq(3)
        freq = self.frequency()
        bifreq = self.nfreq(2)
        trifreq = self.nfreq(3)
        print("\nThe ioc is %f\n" % self.ioc())
        
        print("The top ten letter frequencies are:")
        for i in sf[:10]:
            print(i)
        
        print("\n Graph: \n")
        
        def hashes(n):
            hashes = ""
            for i in range(int(round(n))):
                hashes += "#"
            return hashes
        
        for i in range(65, 91):
            print("%s, %s %f" % (chr(i), hashes(freq[chr(i)] * 400), freq[chr(i)]))
        

        print("The top ten bigram frequencies are:")
        for i in sbf[:10]:
            print(i)
        
        print("The top ten trigram frequencies are:")
        for i in stf[:10]:
            print(i)

    def results(self):
        sf = self.sortedfreq()
        sbf = self.sortednfreq(2)
        stf = self.sortednfreq(3)
        freq = self.frequency()
        bifreq = self.nfreq(2)
        trifreq = self.nfreq(3)


        def hashes(n):
            hashes = ""
            for i in range(int(round(n))):
                hashes += "#"
            return hashes
        

        with open('results.htm', 'w') as f:
            f.write("""
        <!DOCTYPE html>
        <html>
        <head>
        <title>Results</title>  
        </head>
        <body>
        
        <h1>Results</h1>
        
        <h3>Input Message</h3>  
        <p>%s</p>
        
        <h3>Index of Coincidence</h3>  
        <p>The IOC is %f</p>
        
        <h3>The top ten letter frequencies are:</h3>
        
        <table style="width:10%%">
          <tr>
            <th align="left">Letter</th>
            <th align="left">Frequency</th> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
        </table>
        
        
            """ %(self, self.ioc(),
                  sf[0][0], freq[sf[0][0]],
                  sf[1][0], freq[sf[1][0]],
                  sf[2][0], freq[sf[2][0]],
                  sf[3][0], freq[sf[3][0]],
                  sf[4][0], freq[sf[4][0]],
                  sf[5][0], freq[sf[5][0]],
                  sf[6][0], freq[sf[6][0]],
                  sf[7][0], freq[sf[7][0]],
                  sf[8][0], freq[sf[8][0]],
                  sf[9][0], freq[sf[9][0]],
              )
            )
        
        
            f.write("""
        <h3>All letter frequencies:</h3>
        
        
        <table style="width:10%%">
          <tr>
            <th align="left">Letter</th>
            <th align="left">Frequency</th>
            <th align="left"></th>
          </tr>
          <tr>
            <td align="left">A</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th>
          </tr>
          <tr>
            <td align="left">B</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">C</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">D</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">E</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">F</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">G</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">H</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">I</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">J</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">K</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">L</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">M</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">N</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">O</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">P</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">Q</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">R</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">S</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">T</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">U</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">V</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">W</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">X</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">Y</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th> 
          </tr>
          <tr>
            <td align="left">Z</td>
            <td align="left">%.3f</td>
            <td align="left">%s</th>
          </tr>
        </table>
        
        
        
        
        </body>
        </html>
        """ % (freq["A"], hashes(freq["A"] * 400),
               freq["B"], hashes(freq["B"] * 400),
               freq["C"], hashes(freq["C"] * 400),
               freq["D"], hashes(freq["D"] * 400),
               freq["E"], hashes(freq["E"] * 400),
               freq["F"], hashes(freq["F"] * 400),
               freq["G"], hashes(freq["G"] * 400),
               freq["H"], hashes(freq["H"] * 400),
               freq["I"], hashes(freq["I"] * 400),
               freq["J"], hashes(freq["J"] * 400),
               freq["K"], hashes(freq["K"] * 400),
               freq["L"], hashes(freq["L"] * 400),
               freq["M"], hashes(freq["M"] * 400),
               freq["N"], hashes(freq["N"] * 400),
               freq["O"], hashes(freq["O"] * 400),
               freq["P"], hashes(freq["P"] * 400),
               freq["Q"], hashes(freq["Q"] * 400),
               freq["R"], hashes(freq["R"] * 400),
               freq["S"], hashes(freq["S"] * 400),
               freq["T"], hashes(freq["T"] * 400),
               freq["U"], hashes(freq["U"] * 400),
               freq["V"], hashes(freq["V"] * 400),
               freq["W"], hashes(freq["W"] * 400),
               freq["X"], hashes(freq["X"] * 400),
               freq["Y"], hashes(freq["Y"] * 400),
               freq["Z"], hashes(freq["Z"] * 400)))
        
        
            f.write("""
        <h3>The top ten bigram frequencies are:</h3>
        
        <table style="width:10%%">
          <tr>
            <th align="left">Bigram</th>
            <th align="left">Frequency</th> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
        </table>
        """ %(sbf[0][0], bifreq[sbf[0][0]],
              sbf[1][0], bifreq[sbf[1][0]],
              sbf[2][0], bifreq[sbf[2][0]],
              sbf[3][0], bifreq[sbf[3][0]],
              sbf[4][0], bifreq[sbf[4][0]],
              sbf[5][0], bifreq[sbf[5][0]],
              sbf[6][0], bifreq[sbf[6][0]],
              sbf[7][0], bifreq[sbf[7][0]],
              sbf[8][0], bifreq[sbf[8][0]],
              sbf[9][0], bifreq[sbf[9][0]])
            )
        
        
            f.write("""
        <h3>The top ten trigram frequencies are:</h3>
        
        <table style="width:10%%">
          <tr>
            <th align="left">Trigram</th>
            <th align="left">Frequency</th> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
          <tr>
            <td align="left">%s</td>
            <td align="left">%.3f</td> 
          </tr>
        </table>
        """ %(stf[0][0], trifreq[stf[0][0]],
              stf[1][0], trifreq[stf[1][0]],
              stf[2][0], trifreq[stf[2][0]],
              stf[3][0], trifreq[stf[3][0]],
              stf[4][0], trifreq[stf[4][0]],
              stf[5][0], trifreq[stf[5][0]],
              stf[6][0], trifreq[stf[6][0]],
              stf[7][0], trifreq[stf[7][0]],
              stf[8][0], trifreq[stf[8][0]],
              stf[9][0], trifreq[stf[9][0]])
            )
    def fitness(self):
        total = 0
        for count in stdQuadOcc.values():
            total += count
        def score(quad, stdQuadOcc): 
            if quad in stdQuadOcc:
                score = math.log10(float(stdQuadOcc[quad]/total))
            else:
                score = math.log10(0.01/total)
            return score

        fitness = 0
        for i in range(len(self) - 3):
            fitness += score(str(self)[i : i + 4], stdQuadOcc)
        return fitness

    def subDecode(self, keystr):
        '''Decodes the message.
        '''
        keystr = keystr.upper()
        msg = self.inputMessage.upper()
        dec = ""
        for l in msg:
            dec += chr(keystr.index(l) + 65)
        return(ciphertext(dec))

    def optimalKey(self):
        def randSwitch(keystr, msg):
            a = random.randint(0, 25)
            b = random.randint(0, 25)
            while a == b:
                b = random.randint(0, 25)
            if a > b:
                a, b = b, a
            keystr = (keystr[:a] + keystr[b] + keystr[a + 1:b]
                      + keystr[a] + keystr[b + 1:])
            a, b = keystr.index(chr(b + 65)), keystr.index(chr(a + 65))
            newmsg = ""
            for i in str(msg):
		if i == a:
                    i = b
                elif i == b:
                    i = a
                newmsg += i
            return [keystr, ciphertext(newmsg)]

        msg = self
        keystr = "YBXONGSWKCPZFMTDHRQUJVELIA" #Should probably randomize
                                              #at some point
        maxfit = self.subDecode(keystr).fitness()
        iterations = 0
        while iterations < 1000:
            tmp = randSwitch(keystr, msg)
            newkey, msg = tmp[0], tmp[1]
            fit = msg.fitness()
            if fit > maxfit:
                keystr = newkey
                maxfit = fit
                iterations = 0
                print("0")
            else:
                iterations += 1
                print("1")
        return [keystr, maxfit]
    
    def subOptimize(self):
        k = self.optimalKey()
        print(k)
        print(str(self.subDecode(k[0])).lower())


print(ciphertext("""DATJP MZVGG TRVIO OJBZO DIOCZ HDYYG ZJAOC DNTJP RDGGC VQZOJ KVTDF IJRTJ PRDGG WZCPI ODIBH ZVIYD XVIAJ MBDQZ OCZVM MJBVI XZWPO DRDGG IJOAJ MBDQZ TJPMD BIJMV IXZWZ AJMZT JPXVI GZVMI HJMZV WJPOO CZMVO GDIZN AMJHH ZTJPR DGGCV QZOJV NFTJP MXJGG ZVBPZ NDIAM ZIXCV IYWMD ODNCD IOZGG DBZIX ZRCVO OCZTV GMZVY TFIJR KJRZM APGAJ MXZNV MZRJM FDIBO JFZZK OCZMV OGDIZ NMPII DIBVI YRZWJ OCIZZ YOJFI JRRCJ JPMZI ZHDZN VMZWZ AJMZR ZXVIH ZZOTJ PNCJP GYPIY ZMNOV IYOCV ORDOC JPOHZ TJPMD IQZNO DBVOD JINRD GGBVD IGDOO GZIZB JODVO DJINR DOCHZ HVTBV DIZQZ MTOCD IB""").optimalKey())


