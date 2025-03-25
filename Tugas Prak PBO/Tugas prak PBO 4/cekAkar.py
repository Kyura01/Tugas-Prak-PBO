def angka (akar ):
    akar = akar 

    if akar <= 0 :
        return "Akar kuadrat dari nol tidak diperbolehkan"
    else:
        return akar**0.5
    5
try :
    bilangan = (int(input("Masukan angka :")))
    print (angka(bilangan))
except ValueError:
    print ("Input tidak valid. Harap masukan angka yang sesuai")

