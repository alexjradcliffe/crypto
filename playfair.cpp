#include <iostream>
#include <string>

std::string decode(std::string msg, std::string key)
{
    std::string newmsg = "";
    for (int i = 0; i < msg.length() - 1; i += 2){
        char a = msg[i];
        char b = msg[i + 1];
        int pa = key.find(a);
        int pb = key.find(b);
        int ra = pa / 5;
        int rb = pb / 5;
        int ca = pa % 5;
        int cb = pb % 5;
        if (ra == rb){
            ca -= 1;
            cb -= 1;
        } else if (ca == cb){
            ra -= 1;
            rb -= 1;
        } else {
            ca += cb;
            cb = ca - cb;
            ca -= cb; // swaps ca and cb
        }
	if (ra < 0){
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
	if (b != "X"[0]){
	    newmsg += b;
	}
    }
    return newmsg;
}
int main()
{
    std::string msg = "LEXPKEDSTCGUPASAOIQZSQNCUDRPYRCGOSPNHSAVYKTRURQOTSNSGLYQSLSZSYKP";
    std::string key = "PLAYFIRSTUVWXZBCDEGHKMNOQ";
    std::cout << key.substr(0, 5) << std::endl;
    std::cout << key.substr(5, 5) << std::endl;
    std::cout << key.substr(10, 5) << std::endl;
    std::cout << key.substr(15, 5) << std::endl;
    std::cout << key.substr(20, 5) << std::endl;
    std::cout << msg << std::endl;
    std::cout << decode(msg, key) << std::endl;
    std::cout << "harryagai" << std::endl;
}
