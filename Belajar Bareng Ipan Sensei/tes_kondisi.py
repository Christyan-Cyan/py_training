# user_inp = int(input("Masukkan Angka Serah Ganjil Atau Genap "))

# if user_inp % 2 == 0 :
#     print("Angka Yang Anda Masukkan Adalah" ,user_inp, "Termasuk Angka Genap")
# elif user_inp % 2 == 1 :
#     print("Angka Yang Anda Masukkan Adalah", user_inp, "Termasuk Angka Ganjil")
# else :
#     print("Masukkin Angka Anjer")


# Membuat Soal

poin = 0

soal1 = str(input("Ivan Adalah ? "))
if soal1 == "Sensei" :
    print("Anda Benar !\nAnda mendapat 1 Poin")
    poin = poin + 1
else :
    print("Anda Salah")

soal2 = int(input("Berapa Kali Hizbul Terbang Per Hari Nya ? "))
if soal2 == 3 :
    print("Anda Benar !\nAnda mendapat 1 Poin")
    poin = poin + 1
else :
    print("Anda Salah")

soal3 = str(input("Hizbul Adalah ? "))
if soal3 == "Hero" :
    print("Anda Benar !\nAnda mendapat 1 Poin")
    poin = poin + 1
else :
    print("Anda Salah")

soal4 = int(input("Berapa Kali Saya Makan ? "))
if soal4 == 3 :
    print("Anda Benar !\nAnda mendapat 1 Poin")
    poin = poin + 1
else :
    print("Anda Salah")

soal5 = str(input("Siapakah Saya ? "))
if soal5 == "Master" :
    print("Anda Benar !\nAnda mendapat 1 Poin")
    poin = poin + 1
else :
    print("Anda Salah")

print("Poin Anda Adalah : ",poin)