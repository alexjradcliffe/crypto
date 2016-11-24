#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <cmath>
#include <ctime>
#include <vector>

std::map<std::string, int> stdQuadOcc;


void quads(std::map<std::string, int> &stdQuadOcc){
    std::ifstream file("english_quadgrams.txt");
    std::string str;
    int a;
    int total = 0;
    while (std::getline(file, str)){
    	    a = atoi(str.substr(5).c_str());
    	    stdQuadOcc[str.substr(0, 4)] = a;
    	    total += a;
    }
}

int modInv(int x, int mod){
    x %= 26;
    switch(x){
        case 1: return 1;
	case 3: return 9;
        case 5: return 21;
	case 7: return 15;
        case 9: return 3;
	case 11: return 19;
	case 15: return 7;
        case 17: return 23;
	case 19: return 11;
        case 21: return 5;
	case 23: return 23;
	case 25: return 25;
        default: return 0;
    }
}

std::vector<std::vector <int> > modInv(std::vector <std::vector <int> > encKey){
    int det = encKey[0][0] * encKey[1][1] - encKey[0][1] * encKey[1][0];
    int invDet = modInv(det, 26);
    if (invDet == 0){
        std::vector<std::vector <int> > decKey;
        decKey.push_back( std::vector<int>() );
        decKey.push_back( std::vector<int>() );
        decKey[0].push_back(0);
        decKey[0].push_back(0);
        decKey[1].push_back(0);
        decKey[1].push_back(0);
        return decKey;
    } else {
        std::vector<std::vector <int> > decKey;
        decKey.push_back( std::vector<int>() );
        decKey.push_back( std::vector<int>() );
        decKey[0].push_back(encKey[1][1] * invDet);
        decKey[0].push_back(-encKey[0][1] * invDet);
        decKey[1].push_back(-encKey[1][0] * invDet);
        decKey[1].push_back(encKey[0][0] * invDet);
        decKey[0][0] %= 26;
        while (decKey[0][1] < 0) {
            decKey[0][1] += 26;
        }
        decKey[0][1] %= 26;
        while (decKey[1][0] < 0) {
            decKey[1][0] += 26;
        }
        decKey[1][0] %= 26;
        decKey[1][1] %= 26;
        return decKey;
    }
}

std::string decode(std::string msg, std::vector<std::vector <int> >  decKey){
    std::string newmsg = "";
    int l = msg.length();
    for (int i = 0; i < l - 1; i += 2){
        char a = msg[i]; // first character in digraph
        char b = msg[i + 1]; // second character in digraph
        int ia = a;
	int ib = b;
	ia -= 65;
	ib -= 65;	
	int iDecA = (decKey[0][0] * ia + decKey[0][1] * ib) % 26;
	int iDecB = (decKey[1][0] * ia + decKey[1][1] * ib) % 26;
	iDecA += 65;
        iDecB += 65;
	char decA = iDecA;
	char decB = iDecB;
	newmsg += decA;
	newmsg += decB;
    }
    return newmsg;
}

float score(std::string quad){
    if (stdQuadOcc.count("HING") != 1){
        quads(stdQuadOcc);
    }
    if (stdQuadOcc.count(quad) == 1){
        return std::log(stdQuadOcc[quad]);
    } else {
        return std::log(0.01);
    }
}

float fitness(std::string msg){
    float fitness = 0;
    int l = msg.length();
    for (int i = 0; i < l - 3; i++){
        fitness += score(msg.substr(i, 4));
    }
    return fitness;
}

std::vector<std::vector <int> > cribToKey(std::vector<std::vector <int> > ciphertext, std::vector<std::vector <int> > plaintext, bool repeat = false){
    std::vector<std::vector <int> > invCiphertext = modInv(ciphertext);
    if (invCiphertext[0][0] == 0 && invCiphertext[0][1] == 0 && invCiphertext[1][0] == 0 && invCiphertext[1][1] == 0 && repeat == false){
        return modInv(cribToKey(plaintext, ciphertext, true));
    }
    std::vector<std::vector <int> > K;
    K.push_back(std::vector <int>());
    K.push_back(std::vector <int>());
    K[0].push_back((plaintext[0][0] * invCiphertext[0][0] + plaintext[1][0] * invCiphertext[0][1] + 26) % 26);
    K[0].push_back((plaintext[0][0] * invCiphertext[1][0] + plaintext[1][0] * invCiphertext[1][1] + 26) % 26);
    K[1].push_back((plaintext[0][1] * invCiphertext[0][0] + plaintext[1][1] * invCiphertext[0][1] + 26) % 26);
    K[1].push_back((plaintext[0][1] * invCiphertext[1][0] + plaintext[1][1] * invCiphertext[1][1] + 26) % 26);
    return K;
}


void optimize(std::string msg, std::string crib){
    std::vector<std::vector<int> > bestKey;
    bestKey.push_back(std::vector <int>());
    bestKey.push_back(std::vector <int>());
    bestKey[0].push_back(1);
    bestKey[0].push_back(0);
    bestKey[1].push_back(0);
    bestKey[1].push_back(1);
    std::string decMsg = decode(msg, bestKey);
    std::vector<std::vector<int> > newKey = bestKey;
    float maxFit = -1000;
    int l = msg.length();
    for (int i = 0; i < l - 3; i += 2){
        std::vector<std::vector<int> > vCrib;
        vCrib.push_back(std::vector<int>());
        vCrib.push_back(std::vector<int>());
        vCrib[0].push_back(crib[0] - 65);
        vCrib[0].push_back(crib[1] - 65);
        vCrib[1].push_back(crib[2] - 65);
        vCrib[1].push_back(crib[3] - 65);
        std::vector<std::vector<int> > cText;
        cText.push_back(std::vector<int>());
        cText.push_back(std::vector<int>());
        cText[0].push_back(msg[i] - 65);
        cText[0].push_back(msg[i + 1] - 65);
        cText[1].push_back(msg[i + 2] - 65);
        cText[1].push_back(msg[i + 3] - 65);
        newKey = cribToKey(cText, vCrib);
	decMsg = decode(msg, newKey);
	float newFit = fitness(decMsg);
/*	if (newFit > maxFit){
	    bestKey = newKey;
	    maxFit = newFit;
	    std::cout << maxFit << std::endl;
	    std::cout << bestKey[0][0] << " " << bestKey[0][1] << std::endl;
	    std::cout << bestKey[1][0] << " " << bestKey[1][1] << std::endl;
            std::cout << decMsg << std::endl;
            std::cout << std::endl;
	}  */
        bestKey = newKey;
	maxFit = newFit;
	std::cout << i << std::endl;
	std::cout << maxFit << std::endl;
        std::cout << bestKey[0][0] << " " << bestKey[0][1] << std::endl;	        std::cout << bestKey[1][0] << " " << bestKey[1][1] << std::endl;
        std::cout << decMsg << std::endl;
        std::cout << std::endl;
    }
    for (int i = 2; i < l - 3; i += 2){
        std::vector<std::vector<int> > vCrib;
        vCrib.push_back(std::vector<int>());
        vCrib.push_back(std::vector<int>());
        vCrib[0].push_back(crib[1] - 65);
        vCrib[0].push_back(crib[2] - 65);
        vCrib[1].push_back(crib[3] - 65);
        vCrib[1].push_back(crib[4] - 65);
        std::vector<std::vector<int> > cText;
        cText.push_back(std::vector<int>());
        cText.push_back(std::vector<int>());
        cText[0].push_back(msg[i] - 65);
        cText[0].push_back(msg[i + 1] - 65);
        cText[1].push_back(msg[i + 2] - 65);
        cText[1].push_back(msg[i + 3] - 65);
        newKey = cribToKey(cText, vCrib);
        decMsg = decode(msg, newKey);
        float newFit = fitness(decMsg);
/*        if (newFit > maxFit){
	    bestKey = newKey;
	    maxFit = newFit;
	    std::cout << maxFit << std::endl;
	    std::cout << bestKey[0][0] << " " << bestKey[0][1] << std::endl;
	    std::cout << bestKey[1][0] << " " << bestKey[1][1] << std::endl;
            std::cout << decMsg << std::endl;
            std::cout << std::endl;
	}  */
        bestKey = newKey;
	maxFit = newFit;
	std::cout << i - 1 << std::endl;
	std::cout << maxFit << std::endl;
	std::cout << bestKey[0][0] << " " << bestKey[0][1] << std::endl;
	std::cout << bestKey[1][0] << " " << bestKey[1][1] << std::endl;
        std::cout << decMsg << std::endl;
        std::cout << std::endl;
    }
}


int main(){
    std::vector<std::vector <int> > cText;
    cText.push_back(std::vector <int>());
    cText.push_back(std::vector <int>());
    cText[0].push_back(25);
    cText[0].push_back(10);
    cText[1].push_back(10);
    cText[1].push_back(8);
    std::vector<std::vector <int> > pText;
    pText.push_back(std::vector <int>());
    pText.push_back(std::vector <int>());
    pText[0].push_back(5);
    pText[0].push_back(19);
    pText[1].push_back(7);
    pText[1].push_back(4);
    std::vector<std::vector <int> > k = cribToKey(cText, pText); 
    std::cout << k[0][0] << " " << k[0][1] << std::endl;
    std::cout << k[1][0] << " " << k[1][1] << std::endl; 
    std::vector<std::vector <int> > key;
    key.push_back(std::vector <int>());
    key.push_back(std::vector <int>());
    key[0].push_back(3);
    key[0].push_back(17);
    key[1].push_back(8);
    key[1].push_back(25);
    std::cout << key[0][0] << " " << key[0][1] << std::endl;
    std::cout << key[1][0] << " " << key[1][1] << std::endl; 
    std::cout << "\n" << decode("HELLOWORLDDYNAMIX", key) << std::endl;
    std::cout << "\n" << decode("LAMZAMTRGHBANAQK", modInv(key)) << std::endl;
    optimize("LAMZAMTRGHBANAQK", "ELLOW");
    return 0;
}
