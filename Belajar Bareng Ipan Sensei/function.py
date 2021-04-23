# # Belajar Bareng Ipan Sensei
# # Materi Function
# def sapa() :
#     print("Halo Kak")

# sapa()

# nama = "Christyan"

# print(len(nama))

# print(nama.upper())


# # Fungsi Globalisasi (Untuk Memperluas cakupan variabel agar bisa diakses secara global)
# def identitas() :
#     global nama
#     nama = "Christyan"
#     global umur
#     umur = 16
#     print(nama,umur)

# identitas()

# print("Nama Saya", nama ,"\nUmur Saya", umur)


# # Parameter
# def bio(nama,kelas,absen) :
#     print("ello")

# bio("Christyan","XI-SIJA",10)












# Bikin Kalkulator Sederhana

# print("Halo, Selamat Datang Di fitur Kalkulasi Kami")
# tanya = str(input("\nOperasi Hitung Apa Yang Akan Anda Pilih ? "))

# def tambah() :
#     angka1 = int(input("Masukkan Angka "))
#     angka2 = int(input("Masukkan Angka Lagi "))
#     print("Hasilnya adalah", angka1 + angka2)
# def kurang() :
#     angka1 = int(input("Masukkan Angka "))
#     angka2 = int(input("Masukkan Angka Lagi "))
#     print("Hasilnya adalah", angka1 - angka2)
# def kali() :
#     angka1 = int(input("Masukkan Angka "))
#     angka2 = int(input("Masukkan Angka Lagi "))
#     print("Hasilnya adalah", angka1 * angka2)
# def bagi() :
#     angka1 = int(input("Masukkan Angka "))
#     angka2 = int(input("Masukkan Angka Lagi "))
#     print("Hasilnya adalah", angka1 / angka2)
# def pangkat() :
#     angka1 = int(input("Masukkan Angka "))
#     angka2 = int(input("Masukkan Angka Lagi "))
#     print("Hasilnya adalah", angka1 ** angka2)
# def modulus() :
#     angka1 = int(input("Masukkan Angka "))
#     angka2 = int(input("Masukkan Angka Lagi "))
#     print("Hasilnya adalah", angka1 % angka2)

# if tanya == "+" :
#     tambah()
# elif tanya == "-" :
#     kurang()
# elif tanya == "*" :
#     kali()
# elif tanya == "/" :
#     bagi()
# elif tanya == "**" :
#     pangkat()
# elif tanya == "%" :
#     modulus()
# else :
#     print("Dahlah")



# Bikin Kalkulator Sederhana edisi Parameter

print("Halo, Selamat Datang Di fitur Kalkulasi Kami")
tanya = str(input("\nOperasi Hitung Apa Yang Akan Anda Pilih ? "))
angka1 = int(input("Masukkan Angka "))
angka2 = int(input("Masukkan Angka Lagi "))

def tambah(a,b) :
    print("Hasilnya Adalah", a + b)
def kurang(a,b) :
    print("Hasilnya Adalah", a - b)
def kali(a,b) :
    print("Hasilnya Adalah", a * b)
def bagi(a,b) :
    print("Hasilnya Adalah", a / b)
def pangkat(a,b) :
    print("Hasilnya Adalah", a ** b)
def modulus(a,b) :
    print("Hasilnya Adalah", a % b)

if tanya == "+" :
    tambah(angka1,angka2)
elif tanya == "-" :
    kurang(angka1,angka2)
elif tanya == "*" :
    kali(angka1,angka2)
elif tanya == "/" :
    bagi(angka1,angka2)
elif tanya == "**" :
    pangkat(angka1,angka2)
elif tanya == "%" :
    modulus(angka1,angka2)
else :
    print("Dahlah")
