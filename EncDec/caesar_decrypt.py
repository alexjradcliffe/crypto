from __future__ import print_function
from __future__ import division
import sys

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
        
def chi_sq(occC, l):
    occE = freq2occ(stdfreq, l)
    chi_sq = 0
    for i in range(65, 91):
        chi_sq += ((occC[chr(i)] - occE[chr(i)]) ** 2) / occE[chr(i)]
    return chi_sq

def encKey(n):
    '''Produces the encoding key with a shift of n.
    '''
    key = {}
    for i in range(26):
        key[chr(i + 97)] = chr((i + n) % 26 + 65)
    return key

def decKey(n):
    '''Produces the decoding key with a shift of n.
    '''
    key = {}
    for i in range(26):
        key[chr(i + 65)] = chr((i - n) % 26 + 97)
    return key

def encode(msg, n):
    '''Encodes the message.
    '''
    msg = msg.lower()
    enc = ""
    key = encKey(n)
    for l in msg:
        if l in key:
            enc += key[l]
    return(enc)

def decode(msg, n):
    '''Decodes the message.
    '''
    msg = msg.upper()
    dec = ""
    key = decKey(n)
    for l in msg:
        if l in key:
            dec += key[l]
    return(dec)
     

msg = input("Message: ") if python3 else raw_input("Message: ")
msg = """
INGXROK
ZNK TUZK EUA YKTZ UBKX CGY ZXOIQOKX ZNGT O KDVKIZKJ. PGSKROG JOJT’Z PAYZ XKBKXYKZNK CNURK SKYYGMK HKLUXK KTIXEVZOTM OZ, YNK VAZ GRR ZNK VATIZAGZOUT GTJ YVGIOTM HGIQ OT ZNK UXOMOTGR VRGIKY ZU ZNXUC ZNK IGYAGR XKGJKX ULL ZNK YIKTZ. OZ CGYT’Z BKXE YUVNOYZOIGZKJ, HAZ OZ CGY JKBOUAY, GTJ ZKRRY AY YUSKZNOTM GHUAZ ZNK CGE YNKZNOTQY. UTK ZNOTM O GS IKXZGOT GHUAZ, ZNOY JUKYT’Z XKGJ ROQK G YAOIOJK TUZK. CNUCXOZKY UTK UL ZNUYK OT IUJK?

UAX LOKRJ GMKTZ GYQKJ GXUATJ GZ ZNK ATOBKXYOZE GTJ CGY ZURJ ZNGZ PGSKROG’Y HUELXOKTJ CUXQKJ OT ZNK YGSK RGH GY NKX LUX G CNORK. NOY TGSK OY SGXZOT ZXGETUX GTJ ZNKE HUZN JOJ GT OTZKXTYNOV OT ZNKOX YKIUTJ EKGX GZ G YVOTUAZ IUSVGTE IGRRKJ JETGSOD. ZNGZ OY G YSGRR YZGXZAV CNOIN CUXQY UT ZNK LXOTMKY UL ZNK GXSY OTJAYZXE, HAZ TU-UTK YKKSY ZU QTUC SAIN GHUAZ OZ.

O GS TUZ YAXK CNE JETGSOD CUARJ NGBK NOXKJ PGSKROG; EUA YGOJ ZNGZ YNK CGY CUXQOTM UT MXGBOZE CGBKY, CNOIN GXK G YKOYSURUMOIGR VNKTUSKTUT. O XKGJ GT OTZKXKYZOTM VGVKX IGRRKJ “MXGBOZE CGBKY OT KGXZNWAGQKY” CNOIN YAMMKYZKJ ZNGZ ZNKE SOMNZ HK XKYVUTYOHRK LUX ZNK JKYZXAIZOUT UL NOMN XOYK HRUIQY JAXOTM YUSK ZXKSUXY. HAZ ATRKYY JETGSOD GXK VRGTTOTM ZU ZXE ZU CKGVUTOYK KGXZNWAGQKY O GS TUZ YAXK CNE ZNOY CUARJ HK UL OTZKXKYZ ZU ZNKS. CK TKKJ ZU QTUC SUXK GHUAZ NKX CUXQ GTJ CNGZ ZNKE NOXKJ NKX ZU JU.

ZNKXK GXK G RUZ UL WAKYZOUTY KBKT OT ZNK LOXYZ TUZK:

CNE JOJ SGXZOT RKGBK?
CNKXK OY NK?
CNE IUARJT’Z YNK MKZ NURJ UL NOS?
CNGZ CGY ZUU HOM LUX PGSKROG ZU NGTJRK GRUTK?
CNGZ SGJK PGSKROG LKKR MAORZE?
NUC CGY YNK VRGTTOTM ZU LOD OZ?

O GS NUVOTM ZNGZ ZNK GZZGINKJ JUIASKTZ CORR GTYCKX YUSK UL ZNKYK WAKYZOUTY HAZ OZ CORR VXUHGHRE PAYZ XGOYK UZNKXY. O LUATJ OZ VGYZKJ ATJKX ZNK IUBKX UL ZNK TUZKHUUQ ZNGZ ZNK VXKBOUAY SKYYGMK CGY ZGQKT LXUS. O IGT YKK CNE ZNK VUROIK SOYYKJ OZ, ZNUAMN OZ CGYT’Z G BKXE VXULKYYOUTGR PUH.

NGXXE
"""
x = chi_sq(occurences(msg.upper()), len(msg))
n = 0

for i in range(1, 26):
    if chi_sq((occurences(decode(msg, i))), len(msg)) < x:
        n = i
        x = chi_sq(occurences(decode(msg, i)), len(msg))

print(decode(msg, n))
