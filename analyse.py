from __future__ import print_function
from __future__ import division
import operator
import sys


python3 = True if sys.version_info.major > 2 else False
if len(sys.argv) >= 2:
    msg = sys.argv[1]
else:
    msg = input("Enter message: ") if python3 else raw_input("Enter message: ")

msg = """
NRAT IMOS ONNG AAIU GNYO ISOE ETAW RDRG NFOI OLOK RALT EEMU OROL ELYT IWLL IONO NRFA TEST EHIL DAEL TMOC IRNO EFES HOMT GNWI IEME TYNU ITTP PORO HTIS EHOA VTIY AMKL WUCO VEEH IBTE LNID CANI MXAA DTYN AEHR ETDE OUNE LARE AHTW WIYN GLAZ PPZL ABUE SIAR EHTE RTYG BUOM SOLO VOEC LITL LSCA TIPE TIMA EMDI MCUH ISIW THGH TINE SOOM TELA DDOC ULTA HTIT ISCS YLAP HCAM TIEA MTHN HPDI ATUO NOSI ETNW THEH OHUG TVEE RNNI EILO DONE OEPL PIHN GTEV RYEI RNGO YEST HRAE TEOE PLPO BUTA ITON AOFR MNCU HIMT OSOG AHVE DOCU LYTW HEOO NWHK ODNT IREN STPE ATHE SETO EIRT SHCE AUIS TMEM DAKN ELDA IEDT AYNI GLZA SMAI DIED VPSR ODTA APDE TSTE THTH GTAR IDGE OORW TEAA SIWH TTNH AETU THBA MRTS LALY EBOE RTHM ASHR OITG GNAL ITLE RIUO RFOT RSSE ESAL LHTF AIEP DWMS EWAB UOLD CICE SNAE GEHL EPTH LALY EACN RENI KWHE TITA OTOL SIET IREB FONT CIOA FTOR ILFA GDEM ANIH GTTI HTER TCNE AELL IGEI TNTH REIG HSET TVHO ARTY EISK TSHE KTTA CATF HEOO SMET VEEN RLLY PACA TUDO CULT TMHA EYSS TAID NGLB FUIO NACE HAEL CRVA EAHK NWEI IDTH NLUL AFTE TYRI KSPN PMBA EHTE T
"""
msg = msg.upper()
newMsg = ""
for i in range(len(msg)):
    if ord(msg[i]) >= 65 and ord(msg[i]) < 91:
        newMsg += msg[i]
msg = newMsg

    
def occurences(string):
    occ = {chr(i) : 0 for i in range(65, 91)}
    for i in string:
        if i in occ:
            occ[i] += 1
    return occ

def nocc(string, n):
    occ = {}
    for i in range(len(string) + 1 - n):
        if string[i : i + n] in occ:
            occ[string[i : i + n]] += 1
        else:
            occ[string[i : i + n]] = 1
    return occ

def frequency(string):
    N = len(string)
    occ = occurences(string)
    freq = {chr(i) : 0 for i in range(65, 91)}
    for i in occ:
        freq[i] = round(float(occ[i]) / N, 3)
    return(freq)
        

def nfreq(string, n):
    N = len(string) + 1 - n
    occ = nocc(string, n)
    freq = {}
    for i in occ:
        freq[i] = round(float(occ[i]) / N, 3)
    return(freq)
                
def sortedfreq(string):
    freq = frequency(string)
    sortedf = sorted(freq.items(), key=operator.itemgetter(1), reverse=1)
    return sortedf

def sortednfreq(string, n):
    freq = nfreq(string, n)
    sortedf = sorted(freq.items(), key=operator.itemgetter(1), reverse=1)
    return sortedf


def ioc(string):
    N = len(string)
    total = 0
    occ = occurences(string)
    for i in occ:
        total += occ[i] * ( occ[i] - 1 )
    return float(total) / (N * (N - 1))

def hashes(n):
    hashes = ""
    for i in range(int(round(n))):
        hashes += "#"
    return hashes


sf = sortedfreq(msg)
sbf = sortednfreq(msg, 2)
stf = sortednfreq(msg, 3)
freq = frequency(msg)
bifreq = nfreq(msg, 2)
trifreq = nfreq(msg, 3)


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


    """ %(msg, ioc(msg),
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





print("\nThe ioc is %f\n" % ioc(msg))

print("The top ten letter frequencies are:")
for i in sf[:10]:
    print(i)

print("\n Graph: \n")

for i in range(65, 91):
    print("%s, %s %f" % (chr(i), hashes(freq[chr(i)] * 400), freq[chr(i)]))


print("The top ten bigram frequencies are:")
for i in sbf[:10]:
    print(i)

print("The top ten trigram frequencies are:")
for i in stf[:10]:
    print(i)


