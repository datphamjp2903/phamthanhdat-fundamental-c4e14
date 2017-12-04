teencode = {
    "cc": "con cu",
    "loz": "Do dang ghet",
    "Vl": "That la bat ngo",
    "gato": "Ghen an tuc o",
    "wtf": "Cai deo gi vay",
    "xl": "Xam loz, am chi 1 dieu nham nhi",
    "clgt": "Cai lon gi the?",
    "coin card": "Tuong duong voi cc",
    "cmnr": "Con me no roi! Nhan manh y muon noi"
}

while True:
    print(*teencode.keys(), sep=", ")
    code = input("Your code: ").lower()
    print('* '*10)
    if code in teencode:
        print(code)
        print(teencode[code])
    else:
        contribute = input("Not found, do you want to contribute?(Y/N)").lower()
        if contribute == 'y':
            trans = input("Translation: ")
            teencode[code] = trans

    print('* '*10)
