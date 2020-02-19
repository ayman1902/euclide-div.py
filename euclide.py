import os
import time
import sys
def loading():
    clear()
    print("\n" * 5)
    print("        \033[1;32mPlease Wait ===+[\033[34;1m>          \033[1;32m    ]")
    time.sleep(0.4)
    clear()
    print("\n" * 5)
    print("        \033[1;32mPlease Wait ===+[\033[34;1m-->        \033[1;32m     ]")
    time.sleep(0.4)
    clear()
    print("\n" * 5)
    print("        \033[1;32mPlease Wait ===+[\033[34;1m  --->     \033[1;32m     ]")
    time.sleep(0.4)
    clear()
    print("\n" * 5)
    print("        \033[1;32mPlease Wait ===+[\033[34;1m    --->   \033[1;32m     ]")
    time.sleep(0.4)
    clear()
    print("\n" * 5)
    print("        \033[1;32mPlease Wait ===+[\033[34;1m      ---> \033[1;32m     ]")
    time.sleep(0.4)
    clear()
    print("\n" * 5)
    print("        \033[1;32mPlease Wait ===+[\033[34;1m        --->\033[1;32m    ]")
    time.sleep(0.4)
    clear()
    print("\n" * 5)
    print("        \033[1;32mPlease Wait ===+[\033[34;1m          --->\033[1;32m  ]")
    time.sleep(0.4)
    clear()
    print("\n" * 5)
    print("        \033[1;32mPlease Wait ===+[\033[34;1m            --->\033[1;32m]")
    time.sleep(0.4)
    clear()
    print("\n" * 5)
    print("        \033[1;32mPlease Wait ===+[\033[34;1m===============>\033[1;32m]")
    time.sleep(0.4)
    clear()
    print("\n" * 5)
    print(
        "\n\033[1;33m[\033[34;1m*\033[1;33m]\033[1;31mWelcom on\033[35;1m{\033[1;32meuclide-div\033[35;1m}\033[1;31mProgrammable by[\033[34;1mAyman Belhaj\033[1;31m]")
    time.sleep(1)
    try:
        print("\033[34;1m")
        clear()
        print("\n" * 4)
        x = str(input("  Press Any KEY To Continue : "))
        if x == None:
            clear()
    except Exception as e:
        print("\033[1;31mError \033[34;1m: \033[1;32m" + str(e))
        time.sleep(3)
        reload()
    print("\n" * 6)
    print("\033[1;31m                Starting euclide-div...")
    time.sleep(3)
    clear()
def clear():
    try:
        os.system('clear')
        time.sleep(0.5)
    except Exception as e:
        print("\033[1;31mError \033[34;1m: \033[1;32m" + str(e))
        time.sleep(3)
        reload()
def reload():
    clear()
    loading()
    a = int(input("\033[34;1menter \033[1;32ma::"))
    b = int(input("\033[34;1menter \033[1;32mb::"))
    ai, bi = a, b
    if a == 0:
        print("\033[1;31mle pgcd entre", bi, "et 0 est", bi)
        x = int(input(
            "\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes"))
        if x == 0:
            sys.exit()
        if x == 1:
            reload()
    elif b == 0:
        print("\033[1;31mle pgcd entre", ai, "et 0 est", ai)
        x = int(input(
            "\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes"))
        if x == 0:
            sys.exit()
        if x == 1:
            reload()
    elif a == 1:
        print("\033[1;31mle pgcd entre", bi, "et 1 est", 1)
        x = int(input(
            "\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes"))
        if x == 0:
            sys.exit()
        if x == 1:
            reload()
    elif b == 1:
        print("\033[1;31mle pgcd entre", ai, "et 1 est", 1)
        x = int(input(
            "\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes"))
        if x == 0:
            sys.exit()
        if x == 1:
            reload()
    elif a > b:
        a, b = b, a
        while b != 0:
            a, b = b, a % b
            q = (a - a % b) / b
            if (a % b) == 0:
                break
            c = a % b
            print(a, "=", b, "x", q, "+", a % b)
            time.sleep(0.3)
        print("\033[1;31mle pgcd entre", ai, "et", bi, "est", c)
        x = int(input(
            "\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes"))
        if x == 0:
            sys.exit()
        if x == 1:
            reload()
    elif b > a:
        while b != 0:
            a, b = b, a % b
            q = (a - a % b) / b
            if (a % b) == 0:
                break
            c = a % b
            print(a, "=", b, "x", q, "+", a % b)
            time.sleep(0.3)
        print("\033[1;31mle pgcd entre", ai, "et", bi, "est", c)
        x = int(input(
            "\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes"))
        if x == 0:
            sys.exit()
        if x == 1:
            reload()
    elif a == 0 and b == 0:
        print("\033[1;31mpar convention pgcd(0,0) = 0")
        x = int(input(
            "\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes"))
        if x == 0:
            sys.exit()
        if x == 1:
            reload()
clear()
loading()
a = int(input("\033[34;1menter \033[1;32ma::"))
b = int(input("\033[34;1menter \033[1;32mb::"))
ai , bi = a , b
if a == 0:
    print("\033[1;31mle pgcd entre",bi,"et 0 est",bi )
    x = int(input("\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes"))
    if x == 0:
        sys.exit()
    if x == 1:
        reload()
elif b == 0:
    print("\033[1;31mle pgcd entre",ai,"et 0 est",ai )
    x = int(input("\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes ::"))
    if x == 0:
        sys.exit()
    if x == 1:
        reload()
elif a == 1 :
    print("\033[1;31mle pgcd entre",bi,"et 1 est",1 )
    x = int(input("\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes ::"))
    if x == 0:
        sys.exit()
    if x == 1:
        reload()
elif b == 1 :
    print("\033[1;31mle pgcd entre",ai,"et 1 est",1 )
    x = int(input("\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes ::"))
    if x == 0:
        sys.exit()
    if x == 1:
        reload()
elif a > b:
    a , b = b , a
    while b != 0:
        a , b = b , a%b
        q = (a- a%b)/b
        if (a%b) == 0:
            break
        c = a % b
        print(a, "=", b, "x", q, "+", a % b)
        time.sleep(0.3)
    print("\033[1;31mle pgcd entre", ai, "et", bi, "est", c)
    x = int(input(
        "\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes ::"))
    if x == 0:
        sys.exit()
    if x == 1:
        reload()
elif b > a :
    while b != 0:
        a, b = b, a % b
        q = (a - a % b) / b
        if (a % b) == 0:
            break
        c = a % b
        print(a, "=", b, "x", q, "+", a % b)
        time.sleep(0.3)
    print("\033[1;31mle pgcd entre", ai, "et", bi, "est", c)
    x = int(input("\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes ::"))
    if x == 0:
        sys.exit()
    if x == 1:
        reload()
elif a == 0 and b == 0:
    print("\033[1;31mpar convention pgcd(0,0) = 0")
    x = int(input(
        "\033[34;1mdo you wanna repeat \033[34;1m[0]\033[1;32m:\033[35;1m no \033[1;33m| \033[34;1m[1]\033[1;32m:\033[35;1myes ::"))
    if x == 0:
        sys.exit()
    if x == 1:
        reload()
