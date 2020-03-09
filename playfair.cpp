#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <cmath>
#include <ctime>


std::map<std::string, int> stdQuadOcc;


void quads(std::map<std::string, int> &stdQuadOcc){
    // populates stdQuadOcc with all the quadgram frequencies
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

std::string decode(std::string msg, std::string key)
{
    // decodes a message msg given a key
    std::string newmsg = "";
    for (int i = 0; i < msg.length() - 1; i += 2){
        char a = msg[i]; // first character in digraph
        char b = msg[i + 1]; // second character in digraph
        int pa = key.find(a); // position of a in table
        int pb = key.find(b); 
        int ra = pa / 5; // row of a
        int rb = pb / 5;
        int ca = pa % 5; // column of a
        int cb = pb % 5;
        if (ra == rb){ // same row
            ca -= 1;
            cb -= 1;
        } else if (ca == cb){ // same column
            ra -= 1;
            rb -= 1;
        } else { // opposite corners
            ca += cb;
            cb = ca - cb;
            ca -= cb; // swaps ca and cb
        }
	if (ra < 0){ // makes sure everything is positive
	    ra += 5;
	}
        if (rb < 0){
	    rb += 5;
	}
        if (ca < 0){
	    ca += 5;
	}
	if (cb < 0){
	    cb += 5;
	}

        pa = 5 * ra + ca;
        pb = 5 * rb + cb;
        a = key[pa];
	b = key[pb];
	newmsg += a;
	if (b != "X"[0]){ // X is used to break double letter
	    newmsg += b;
	}
    }
    return newmsg;
}

float score(std::string quad){
    if (stdQuadOcc.count("HING") != 1){
        quads(stdQuadOcc);
    } // checks that stdQuadOcc has been populated
    if (stdQuadOcc.count(quad) == 1){
        return std::log(stdQuadOcc[quad]);
    } else {
        return std::log(0.01);
    }
}

float fitness(std::string msg){
    // returns the fitness of a message
    float fitness = 0;
    for (int i = 0; i < msg.length() - 3; i++){
        fitness += score(msg.substr(i, 4));
    }
    return fitness;
}

void randSwitch(std::string &key){
    // switches two random characters in the key
    std::srand(std::time(0));
    int a = std::rand() % 25;
    int b;
    do {
        b = std::rand() % 25;
    } while (a == b);
    if (a > b){
        a += b;
        b = a - b;
	a -= b; // still switches a and b
    }
    char tmp = key[a];
    key[a] = key[b];
    key[b] = tmp;
}

void optimize(std::string msg){
    // performs a greedy random search on the message for the best key
    std::string bestKey = "YBXONGSWKCPZFMTDHRQUJVELIA"; // random key used to start the search
    std::string decMsg = decode(msg, bestKey);
    std::string newKey = bestKey;
    float maxFit = fitness(decMsg);
    int iterations = 0;
    while (iterations < 1000){ // increase this if it isn't working
        randSwitch(newKey);
	std::string decMsg = decode(msg, newKey);
	float newFit = fitness(decMsg);
	if (newFit > maxFit){
	    bestKey = newKey;
	    maxFit = newFit;
	    iterations = 0;
	} else {
	    iterations += 1;
	}
    std::cout << bestKey << " " << maxFit << std::endl;
    std::cout << decode(msg, bestKey) << std::endl;
    std::cout << std::endl;
    }
}

int main(){
    optimize("GYSWOBGKZGXSTYGKTZOEHGQCKCFHLXRHFWHUEPIGLXHNTNGFNSENCKLICQCFCNMXPSDGKEUFYLNFSLYLNECQHEPSOPNFUHNFIHWMGHDKRHNCSIOWEPHGQCYXVZNTOHYLFNDPUNNHCNCQYHPTMLRTIHWFHXTUFSCQGKYVGYIGFIEGHNKZQCKCSBGYHSOTFGOXEDHFZOXOIHBYPVFPINCKEDXHSFOXEDHKEPYTEFFSKBSESLVYYXXSTYYKTNRHTFRLBQHEPFNSNPUFYLYLHFFSKBKCVULTPFUHNXCXIHEPZQSFUTYHOEBQSZSTQLGHGYXEGYWRCKPDXSTYGAFSXNYTYKHUTUNHYMBYMNZGNOIHXHNTNONFHTVXFSHXOBEDHVTYQBANIHPMRTKCTFHDFCBYMAVUGFXIXCOCPTXFSFHRTSNHKDGDNCGXFSHTSNCNNOFCHYIHOXPSZBYRVUTUIHUHVYDEYXWPSXPTUTYLYVIHSQBQYHSNXGWRZKHGUTYTYLNXIGOUIHAHTYIHDKZUCZGKSTPLOXQBEDYMSYDGKEYLISYVLYTYIHLPANEDCKZYCQNXEDENOEFXCQWOZHKEYTOEGQHSEWGBVYHDYVTUIHUHNFOENXVYCHPZLKFSYSXGWMPSBVIGNHCKMUCQUDANINZUCZBCPFUHOEGKNSUTWOZHKEYTNHGAHXIHYSXDWOBTHUIEYKXNQZSISOYLHCXFSFFDQSNXCXINCZIHPFDEUHYVGUFSNEPWHUINIHQBLKYLFSNXUHOEEPYTOBYLFCBCHOSLOXSLFSGCNTOHPDKIPLRTMXHULYIHOEDUOEHXHNTNRNHXLTVILHPTSNXGSBCKXHNTMTHUIEGHDKGKNSXOEDCKZYCQNXIHEPZVXNIWMYSPZKYTGYXGSLYRBQPDUFNTKHHXIHOWSYSLVYYXHTZPFPNEYOHO");
    return 0;
}
