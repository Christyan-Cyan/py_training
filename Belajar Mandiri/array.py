kondisi = True
basic = ["ipan suki", "maman", "hizbool", 'cyan']

def fungsi() :
    inp = input("siapa yg ingin di eksekusi? ")

    for i in basic :
        if i == inp :
            print(i + " telah rip")
            break
    else :
        print("ok sip")

while kondisi == False :
    fungsi()
    if inp == "end" :
        break