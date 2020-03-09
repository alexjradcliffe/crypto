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
    if ord(msg[i]) > 64 and ord(msg[i]) < 91:
        newMsg += msg[i]
msg = newMsg

    
def occurences(string):
    """
        Returns the number of occurences of each character in each string in a dict.
    """
    occ = {chr(i) : 0 for i in range(65, 91)}
    for i in string:
        if i in occ:
            occ[i] += 1
    return occ


def ioc(string):
    """
        Returns the index of coincidence of a string
    """
    N = len(string)
    total = 0
    occ = occurences(string)
    for i in occ:
        total += occ[i] * ( occ[i] - 1 )
    return float(total) / (N * (N - 1))


def avgioc(string, n):
    """
        Splits the string into n columns, and returns the average ioc of each column
    """
    columns = ["" for i in range(n)]
    for i in range(len(string)):
        columns[i % n] += string[i]
    avgioc = 0
    for column in columns:
        avgioc += ioc(column) / n
    return avgioc


print("\nThe column IOC's are:\n")

for i in range(12):
    print(i + 1, avgioc(msg, i + 1) * 26)
    # This should tell you what the likely length of the keystring is
