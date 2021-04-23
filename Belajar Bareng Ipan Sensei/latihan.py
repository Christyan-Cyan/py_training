kondisi = True
basic = ["ipan suki", "maman", "hizbool", 'cyan']


def fungsi(inp) :

    for i in basic :
        if i == inp :
            print(i + " telah rip")
            break
    else :
        print("ok sip")

while kondisi :
    inp = input("siapa yg ingin di eksekusi? ")
    if inp == "end":
        kondisi = False
    else:
        fungsi(inp)