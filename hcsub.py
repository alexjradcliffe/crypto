from __future__ import print_function
from __future__ import division
import operator
import sys
import math
import random


python3 = True if sys.version_info.major > 2 else False
if len(sys.argv) >= 2:
    msg = sys.argv[1]
else:
    msg = input("Enter message: ") if python3 else raw_input("Enter message: ")
msg = """
RTBFX UIUHT UZWUW ZAMMT BHUGS AUZSA ZEJHU ZIILH ARTIR WBNIM HTUZS GEINA FIUFI CAFHM IYBPT BKIBZ ACCAF HJZUH PTIFI URTIR WILHT IRUCT IFRXI FWGEB RWSFA JZLBZ LUHHJ FZGAJ HGTIU GMTUH IFJGG UBZTI FNBYU XPXIN HYAGR AMUZE JHGTI TBGFI XBHUK IGUZH TISJX BSBHC IFYGT IRXIB FXPTB GZAXA KINAF HTIGA KUIHS AKIFZ YIZHG AUBYG HUXXZ AHGJF IMTAG TIMBG MAFWU ZSNAF EJHUH TUZWH TUGUG WIPUZ HIXXU SIZRI UZHTI YIBZH UYIUT BKIEI IZMBH RTUZS HTIEF UHGHT IPGII YHATB KIEII ZUZRA ZHBRH MUHTA JFNFU IZLGU ZHTIF IURTG LAWHA FBZLH TIPUZ HJFZT BKIEI IZMBH RTUZS HTINF IZRTU HGIIY GXUWI MIBFI BXXMA FWUZS BSBUZ GHAZI BZAHT IFMTU RTUFI BXXPL ULZHI OCIRH BZLSU KIZMT BHMIF IBLUZ HTINF IZRTL ARJYI ZHXBG HMIIW ULAZH HTUZW HTBHU GBRAU ZRULI ZRIYP AMZSJ IGGUG HTBHH TIFJG GUBZG WZAMM TBHUG SAUZS AZBZL HTBHA JFEIG HTACI ANJZR AKIFU ZSUHU GHAEF IBWUZ HAHTI UFTDB ZLHFP HANUZ LGAYI HTUZS HTIFI JZNAF HJZBH IXPBR RAFLU ZSHAY PGAJF RIPJF UHTIP TBKIH BWIZH AJGUZ SBZIM RUCTI FGAXU HBUFI NAFBF RTUKI GHAFB SIANH ACGIR FIHNU XIGGA IKIZU NMIYB ZBSIH AGHIB XHTIF IXIKB ZHNUX IUHMU XXHBW IBXAH ANRAY CJHUZ SHAEF IBWHT IRUCT IFUBH HBRTB EFUIN YIGGB SINFA YPJFU IZRFP CHILJ GUZSB ZBYGR ARUCT IFWIP MAFLX IZSHT UGGUO UZMTU RTTIL IGRFU EIGHT IRUCT IFUHU GKIFP RXIKI FGUYC XIHAU YCXIY IZHEJ HBLIK UXHAR FBRWB ZLYPA ZITAC IUGHT BHMIR BZBXG ANUZL HTIRU CTIFW IPMTU XIUZH TITDA FBHXI BGHCB FHANU HUCXB ZHAIZ HIFUZ HMAMI IWGAZ LIRIY EIFGU OHIIZ HTHTI FJGGU BZGBF ITAGH UZSBX BFSIC FACBS BZLBI KIZHB GCBFH ANHTI UZHIF ZBHUA ZBXIE BJBJG GHIXX JZSMU HTXIB LUZSC AXUHE JFAYI YEIFG UZBHH IZLBZ RIYAG HANHT IGIRJ FUHPH IBYMU XXEIA RRJCU ILMUH THTBH BZLTD GIRJF UHPMU XXEIF IXBHU KIXPX USTHM UHTXJ RWUMU XXSIH UZBZL AJHMU HTHTI NUXIG MIZII LHTBH ZUSTH BZLHT IZMIR BZSIH HAHTI EAHHA YANHT IMTAX IFIUR TGLAW HAFGH FBHBS IYBXX HTIEI GHTBF FP


"""

msg = msg.upper()
newMsg = ""
for i in range(len(msg)):
    if ord(msg[i]) > 64 and ord(msg[i]) < 91:
        newMsg += msg[i]
msg = newMsg

with open('english_quadgrams.txt') as f:
    lines = f.read().splitlines()

stdQuadOcc = {}
for line in lines:
    stdQuadOcc[line.split()[0]] = int(line.split()[1])

total = 0
for count in stdQuadOcc.values():
    total += count

def score(quad):
    if quad in stdQuadOcc:
        score = math.log10(float(stdQuadOcc[quad]/total))
    else:
        score = math.log10(0.01/total)
    return score

def decode(msg, keystr):
    '''Decodes the message.
    '''
    keystr = keystr.upper()
    msg = msg.upper()
    dec = ""
    for l in msg:
        dec += chr(keystr.index(l) + 65)
    return(dec)

def fitness(msg, keystr):
    msg = decode(msg, keystr)
    fitness = 0
    for i in range(len(msg) - 3):
        fitness += score(msg[i : i + 4])
    return fitness

def randSwitch(keystr):
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
    k = optimize(msg, "YBXONGSWKCPZFMTDHRQUJVELIA")
    print(k)
    print(decode(msg, k[0]).lower())

