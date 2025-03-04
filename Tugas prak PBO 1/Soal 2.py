
siswa = {}

jmlh_siswa = int(input("Input jumlah siswa "))

for i in range(1, jmlh_siswa + 1):
    nama = input("Masukkan nama siswa ke- {i}: ")
    nilai = int(input("Masukkan nilai untuk {nama}: "))
    siswa[nama] = nilai

print("Data Dictionary =", siswa)