print("\nKALKULATOR SUHU\n")
pilih = str(input("Pilih Suhu Yang Ingin Anda KKonversikan "))

def c_convert() :
    print("\nKONVERSI CELCIUS\n")
    celcius = float(input("Berapa Suhu Celcius Yang Ingin Anda Konversikan ? "))
    print("")

    # Suhu dalam Reamur
    reamur = (4/5) * celcius
    print(celcius, "Celcius jika dikonversikan Ke Reamur adalah", reamur, "Reamur")

    # Suhu dalam Fahrenheit
    fahrenheit = ((9/5) * celcius) + 32
    print(celcius, "Celcius jika dikonversikan Ke Fahrenheit adalah", fahrenheit, "Fahrenheit")

    # Suhu dalam Kelvin
    kelvin = celcius + 273
    print(celcius, "Celcius jika dikonversikan Ke Kelvin adalah", kelvin, "Kelvin\n")


def r_convert() :
    print("\nKONVERSI REAMUR\n")
    reamur = float(input("Berapa Suhu Reamur Yang Ingin Anda Konversikan ? "))
    print("")

    # Suhu Dalam Celcius
    celcius = (5/4) * reamur
    print(reamur, "Reamur jika dikonversikan ke Celcius adalah", celcius, "Celcius")

    # Suhu Dalam Fahrenheit
    fahrenheit = ((9/4) * reamur) + 32
    print(reamur, "Reamur jika dikonversikan ke Fahrenheit adalah", fahrenheit, "Fahrenheit")

    # Suhu Dalam Kelvin
    kelvin = ((5/4) * reamur) + 273
    print(reamur, "Reamur jika dikonversikan ke Kelvin adalah", kelvin, "Kelvin\n")


def f_convert() :
    print("\nKONVERSI FAHRENHEIT\n")
    fahrenheit = float(input("Berapa Suhu Fahrenheit Yang Ingin Anda Konversikan ? "))
    print("")

    # Suhu Dalam Celcius
    celcius = 5/9 * (fahrenheit - 32)
    print(fahrenheit, "Fahrenheit jika dikonversikan ke Celcius adalah", celcius, "Celcius\n")

    # Suhu Dalam Reamur
    reamur = 4/9 * (fahrenheit - 32)
    print(fahrenheit, "Fahrenheit jika dikonversikan ke Reamur adalah", reamur, "Reamur\n")

    # Suhu Dalam Kelvin
    kelvin = (5/9 * (fahrenheit - 32)) + 273
    print(fahrenheit, "Fahrenheit jika dikonversikan ke Kelvin adalah", kelvin, "Kelvin\n")


def k_convert() :
    print("\nKONVERSI KELVIN\n")
    kelvin = float(input("Berapa Suhu Kelvin Yang Ingin Anda Konversikan ? "))
    print("")

    # Suhu Dalam Celcius
    celcius = kelvin - 273
    print(kelvin, "Kelvin jika dikonversikan ke Celcius adalah", celcius, "Celcius\n")

    # Suhu Dalam Reamur
    reamur = 4/5 * (kelvin - 273)
    print(kelvin, "Kelvin jika dikonversikan ke Reamur adalah", reamur, "Reamur\n")

    # Suhu Dalam Kelvin
    fahrenheit = ((9/5) * (kelvin - 273)) + 32
    print(kelvin, "Kelvin jika dikonversikan ke Kelvin adalah", fahrenheit, "Fahrenheit\n")


if pilih == "celcius" :
    c_convert()
elif pilih == "reamur" :
    r_convert()
elif pilih == "fahrenheit" :
    f_convert()
elif pilih == "kelvin" :
    k_convert()
else :
    print("Nggak Ada Anying")