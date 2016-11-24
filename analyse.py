from __future__ import print_function
from __future__ import division
import operator
import sys


python3 = True if sys.version_info.major > 2 else False
if len(sys.argv) >= 2:
    msg = sys.argv[1]
else:
    msg = input("Enter message: ") if python3 else raw_input("Enter message: ")

msg = """ANROH AESTM VEYES HAEKS TKCEH VRTEA EEHRK NLNND EBMSS OBOGN HAIOR GLASU SAFAU AIUAA ONAEG EEPTM DFLTE HESOE ARFME EOTAE LSAPA ATLIK ENHAI SETIZ AAEAH EOBOT TNTDR TLTFA SVNED SRNWT ASETO DLLNY DELOS ELLTP IKEHW LOOTC TTAEY ITSRR HANER MAIAS EDDAI ADEAI MBTLO RUAUA NUHNT MTTMO TGWUS LTSOF YASED UALSO ODESY SNUNA GDAPO DAEEI SLGEC KBUCR HUIEG OYIRI PEMNR DLTTN EPHEE FIASE MTAEO IILEE GATNR OEEIM YTCDN UETEH EROIE NNSIR YTTLE TUSTG GCMSU TCTAH EETIA IESDA HENSG VOERS NHSTI ORTDB HETSA EEBHE RTLEY NSGEE HEREH TOETH EDTTE EICEE STATT ELIFW OIEPB MEUEJ IDOHT TIAED VMHUS SDTSN OEIKA SCDTI LVCTC EASCV EDNNI EIOTU TLRTO SEDWA HOURE EITIA HEHAF CTBIT SYMNO TREOF DTELA ONUOA KMSCI DESHT STISE RSTSU BGELH XEIYH EUMIT NTHAL ACOYX ODIAT AEHLD AAMFL EOGSA NATRJ IAMVN IMGAT TRIAN ICNWH SBUIT YLCTE IEEDW BESOF HOESD AIOSC SFINO MUENT KETUF NOILF ASVNB ESSFT OSESV NAWOR IPOFH AEBHE TTLVD NOEBT BLUAK ECECF FADMS AONIE ACOER ODEHE EDNIH VHYNE PVAHO METTL AWICA ITWHE GEEHA OTATE EHLER EHILC HAGMR MVREE TIGYO ETFAR OEEIY OSIDT THADT OSOOU TIASI OHNUT SIRMA NRCRT RYRCI MIDDE EICUH CTDIW NDHNT LYAEB HUOPR WNOME EATTL EEAEK NNDOG USEAF IDETS ABAOK EANHH HVAND HSCGT HMTAD LTEIR OFAEE HHEFE MAOEA LLCOD AAEEH EIODT EMMAE MDPEH NSETW HAISN ILRIK BHAIF AOHOK NTSEI CNAAL POHHS NCREE EMTHD EYGTR FEIBO OHGSE COILT EHENT IKGGN SHTIS EITTR TIKAG CELNT RNREE AIRCO UNMSG EERHO VNRLN IKNNT SHNEM UIWSS WBOTI PIFEI TESEE OLETT THAAN CENOD IARLV ETNNR UTCOD TAAAS TBPEA ROTIA NAYAA MTEWN ITTHO PNLDR OTHEW OTNLJ ICOMN YMBIU YENIA WTHUN NREEO HLDFW GCTWE TATID OKOTT EEHUF IWFHR CSTEF TIISD AFIAR DAAEH AEEOO UDASU SNTSA RDHIY NMEOP RENRC EUCSF ONAHL BCTEE ECHEI ETTGE SHAEB HHOMT HETTC TTBMS HMRDA ALIDT MNIEO IAOST ELESH LBPNT OLNEM RIEBO TNIWO TRMHR PUUGW TCUTN ETTHG NIAVE HINII"""
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


