kondisi = True
basic = ["ipan suki", "maman", "hizbool", 'cyan']

inp = input("siapa yg ingin di eksekusi? ")

def fungsi(inp) :

    for i in basic :
        if i == inp :
            print(i + " telah rip")
            break
    else :
        print("ok sip")

while kondisi :
    if inp == "end":
        kondisi = False
    else:
        fungsi(inp)