a = int(input("enter a::"))
b = int(input("enter b::"))
ai , bi = a , b
if a == 0:
    print("le pgcd entre",bi,"et 0 est",bi )
elif b == 0:
    print("le pgcd entre",ai,"et 0 est",ai )
elif a == 1 :
    print("le pgcd entre",bi,"et 1 est",1 )
elif b == 1 :
    print("le pgcd entre",ai,"et 1 est",1 )
elif a > b:
    a , b = b , a
    while b != 0:
        a , b = b , a%b
        q = (a- a%b)/b
        if (a%b) == 0:
            break
        c = a % b
        print(a, "=", b, "x", q, "+", a % b)
    print("le pgcd entre", ai, "et", bi, "est", c)
elif b > a :
    while b != 0:
        a, b = b, a % b
        q = (a - a % b) / b
        if (a % b) == 0:
            break
        c = a % b
        print(a, "=", b, "x", q, "+", a % b)
    print("le pgcd entre", ai, "et", bi, "est", c)
elif a == 0 and b == 0:
    print("par convention pgcd(0,0) = 0")

