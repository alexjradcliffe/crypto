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
ANROHAESTMVEYESHAEKSTKCEHVRTEAEEHRKNLNNDEBMSSOBOGNHAIORGLASUSAFAUAIUAAONAEGEEPTMDFLTEHESOEARFMEEOTAELSAPAATLIKENHAISETIZAAEAHEOBOTTNTDRTLTFASVNEDSRNWTASETODLLNYDELOSELLTPIKEHWLOOTCTTAEYITSRRHANERMAIASEDDAIADEAIMBTLORUAUANUHNTMTTMOTGWUSLTSOFYASEDUALSOODESYSNUNAGDAPODAEEISLGECKBUCRHUIEGOYIRIPEMNRDLTTNEPHEEFIASEMTAEOIILEEGATNROEEIMYTCDNUETEHEROIENNSIRYTTLETUSTGGCMSUTCTAHEETIAIESDAHENSGVOERSNHSTIORTDBHETSAEEBHERTLEYNSGEEHEREHTOETHEDTTEEICEESTATTELIFWOIEPBMEUEJIDOHTTIAEDVMHUSSDTSNOEIKASCDTILVCTCEASCVEDNNIEIOTUTLRTOSEDWAHOUREEITIAHEHAFCTBITSYMNOTREOFDTELAONUOAKMSCIDESHTSTISERSTSUBGELHXEIYHEUMITNTHALACOYXODIATAEHLDAAMFLEOGSANATRJIAMVNIMGATTRIANICNWHSBUITYLCTEIEEDWBESOFHOESDAIOSCSFINOMUENTKETUFNOILFASVNBESSFTOSESVNAWORIPOFHAEBHETTLVDNOEBTBLUAKECECFFADMSAONIEACOERODEHEEDNIHVHYNEPVAHOMETTLAWICAITWHEGEEHAOTATEEHLEREHILCHAGMRMVREETIGYOETFAROEEIYOSIDTTHADTOSOOUTIASIOHNUTSIRMANRCRTRYRCIMIDDEEICUHCTDIWNDHNTLYAEBHUOPRWNOMEEATTLEEAEKNNDOGUSEAFIDETSABAOKEANHHHVANDHSCGTHMTADLTEIROFAEEHHEFEMAOEALLCODAAEEHEIODTEMMAEMDPEHNSETWHAISNILRIKBHAIFAOHOKNTSEICNAALPOHHSNCREEEMTHDEYGTRFEIBOOHGSECOILTEHENTIKGGNSHTISEITTRTIKAGCELNTRNREEAIRCOUNMSGEERHOVNRLNIKNNTSHNEMUIWSSWBOTIPIFEITESEEOLETTTHAANCENODIARLVETNNRUTCODTAAASTBPEAROTIANAYAAMTEWNITTHOPNLDROTHEWOTNLJICOMNYMBIUYENIAWTHUNNREEOHLDFWGCTWETATIDOKOTTEEHUFIWFHRCSTEFTIISDAFIARDAAEHAEEOOUDASUSNTSARDHIYNMEOPRENRCEUCSFONAHLBCTEEECHEIETTGESHAEBHHOMTHETTCTTBMSHMRDAALIDTMNIEOIAOSTELESHLBPNTOLNEMRIEBOTNIWOTRMHRPUUGWTCUTNETTHGNIAVEHINII
"""[:50]

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

def columns(msg, l):
    columns = ["" for i in range(l)]
    for i in range(len(msg)):
        columns[i % l] += msg[i]
    return columns

def decode(msg, keystr):
    '''Decodes the message.
    '''
    dec = ""
    l = len(keystr)
    encCols = columns(msg, l)
    decCols = ["" for i in range(l)]
    for i in range(l):
        decCols[int(keystr[i])] = encCols[i]
    for j in range(len(decCols[-1])): #column length
        for i in range(l): #row
            try:
                dec += decCols[i][j]
            except IndexError:
                break
    return(dec)

def fitness(msg, keystr):
    msg = decode(msg, keystr)
    fitness = 0
    for i in range(len(msg) - 3):
        fitness += score(msg[i : i + 4])
    return fitness

def randSwitch(keystr):
    l = len(keystr)
    a = random.randint(0, 2 * l)
    if a == l:
        nums = [x for x in range(10)]
        random.shuffle(nums)
        parent = ""
        for i in nums:
            parent += str(i)
        return parent
    elif a > l:
        return keystr[a - l:] + keystr[: a - l]
    else:
        b = random.randint(0, l - 1)
        while a == b:
            b = random.randint(0, l - 1)
	tmp = keystr[b]
        keystr = keystr[:b] + keystr[b + 1:]
	keystr = keystr[:a] + tmp + keystr[a:]
        return keystr

def optimize(msg, keystr):
    maxfit = fitness(msg, keystr)
    iterations = 0
    while iterations < 50000:
        newkey = randSwitch(keystr)
        if fitness(msg, newkey) > maxfit:
            keystr = newkey
            maxfit = fitness(msg, keystr)
            iterations = 0
        else:
            iterations += 1
    return [keystr, maxfit]


maxf = -1000000
while True:
    nums = [x for x in range(10)]
    random.shuffle(nums)
    parent = ""
    for i in nums:
       parent += str(i)
    k = optimize(msg, parent)
    if True:
        print(msg)
        print(k)
        print(decode(msg, k[0]).lower())
	maxf = int(k[0])

