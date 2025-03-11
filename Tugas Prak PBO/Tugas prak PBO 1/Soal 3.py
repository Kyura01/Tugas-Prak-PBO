nama = input("Input Nama : ")
nim = input("Input Nim : ")
kata = input("Input resolusi atau kata kata : ")

nama_file = "me.txt"

with open (nama_file, "w") as n:
    n.write(f"Nama : {nama}\n")
    n.write(f"Nim : {nim}\n")
    n.write(f"Resousi : {kata}\n")

    print (f"file {nama_file} berhasil dibuat !!")