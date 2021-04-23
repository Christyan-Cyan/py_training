data = int(input("Masukkan Angka Kesukaanmu "))

if data == 5 :
    print("Angka Yang Anda Masukkan Sama Dengan Angka Kesukaan Saya yaitu", data )
elif data < 5 :
    print("Angka Favorit Anda Kurang Dari Angka Favorit Saya")
else :
    print("Angka Favorit Anda Adalah", data)



# Pengkondisian Event Harian
print("\nAnda Punya Beberapa Kegiatan Minggu Ini\n")

hari = input("Hari Apakah Hari Ini ? ")

if hari == "Senin" :
    print("Teman Anda Berulang Tahun Hari Ini, Anda Harus Datang !")
elif hari == "Selasa" :
    print("Anda Akan Mendatang Grand Opening Restoran Seafood Di Dekat Rumah Anda agar Dapat Makanan Gratis")
elif hari == "Rabu" :
    print("Anda Harus Melaksanakan Kegiatan Tahunan Di Sekolah")
elif hari == "Kamis" :
    print("Anda akan Menjalani Ritual Wajib !")
elif hari == "Jum'at" :
    print("Anda ada Kelas Wajib Sore Ini !")
elif hari == "Jumat" :
    print("Anda ada Kelas Wajib Sore Ini !")
elif hari == "Sabtu" :
    print("Anda Harus Berdiam Diri Di Rumah Malam Ini Demi Kebaikan Anda")
elif hari == "Minggu" :
    print("Anda Hanya Harus Tidur Untuk Mempersiapkan Diri Hari Esok")
else :
    print("Dahlah")


