import math

class Kalkulator:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, other):
        return Kalkulator(self.nilai + other.nilai)

    def __sub__(self, other):
        return Kalkulator(self.nilai - other.nilai)
    
    def __mul__ (self, other):
        return Kalkulator(self.nilai * other.nilai)
    
    def __truediv__(self, other):
        if other.nilai == 0:
            raise ValueError("Tidak Bisa Membagi dengan 0")
        return Kalkulator(self.nilai / other.nilai)
    
    def __pow__(self, other):
        return Kalkulator(self.nilai ** other.nilai)
    
    def log(self, other):
        if self.nilai <= 0 or other.nilai <= 0:
            raise ValueError("Tidak Bisa Menghitung Logaritma dari 0 atau bilangan negatif")
        return Kalkulator(math.log(self.nilai, other.nilai))
    
    def __str__(self):
        return str(self.nilai)

print("Kalkulator sederhana : ")
print("1. + ")
print("2. -")
print("3. x")
print("4. :")
print("5. **")
print("6. log")

pilih = input("Masukan pilihan anda : ")

nilai = int(input("Masukan nilai 1 "))
nilai = Kalkulator(nilai)

other = int(input("Masukan nilai 2: "))
other = Kalkulator(other)

if pilih == "1":
    hasil_penjumlahan = nilai + other
    print(f"Hasil Penjumlahan: {hasil_penjumlahan}")

elif pilih == "2":
    hasil_pengurangan = nilai - other
    print(f"Hasil Pengurangan: {hasil_pengurangan}")

elif pilih == "3":
    hasil_perkalian = nilai * other
    print(f"Hasil Perkalian: {hasil_perkalian}")
          
elif pilih == "4":
    hasil_pembagian =  nilai / other
    print(f"Hasil Pembagian: {hasil_pembagian}")

elif pilih == "5":
    hasil_eksponen = nilai ** other
    print(f"Hasil Eksponen: {hasil_eksponen}")

elif pilih == "6":
    hasil_logaritma = nilai.log(other)
    print(f"Hasil Logaritma: {hasil_logaritma}")

else:
    print("Pilihan tidak ada cuy")