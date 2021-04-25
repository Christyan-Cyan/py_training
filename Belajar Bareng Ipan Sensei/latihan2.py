data = list()

while True :
    tanya = input("Apakah Anda Ingin Menambah Data ? ")
    if tanya == "ya" :
        inp_data = input("Masukkan Data ")
        data.append(inp_data)
    elif tanya == "tidak" :
        print("Ini Adalah Data Milik Anda", data, "Panjang Data = ",len(data))
        break
    else :
        print("Apa itu ? Saya Tidak Paham")

