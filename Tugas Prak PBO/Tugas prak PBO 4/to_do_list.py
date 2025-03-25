class crud:
    def __init__(self):
        self.tugas = []

    def add_tugas(self, tugas):
        self.tugas.append(tugas)

    def remove_tugas(self, index):
        if 0 <= index < len(self.tugas):
            self.tugas.pop(index)
        else:
            raise IndexError ("Tugas tidak ditemukan")

    def get_tugas(self):
        return self.tugas
    
    def exit(self):
        pass

def main():
    c = crud()
    while True:
        print("\nMenu")
        print("1. Add tugas")
        print("2. Remove tugas")
        print("3. List tugas")
        print("4. Exit")
        choice = input("Masukan pilihan : ")

        if choice == "1":
            tugas = input("Massukan Tugas: ")
            c.add_tugas(tugas)

        elif choice == "2":
            print("List index tugas : ")
            for i, tugas in enumerate(c.get_tugas()):
                print(f"{i}. {tugas}")

            try:
                index = int(input("Masukan index tugas yang ingin dihapus: "))
                c.remove_tugas(index)
            except ValueError:
                print("Input tidak valid. Harap masukan angka")

        elif choice == "3":
            for tugas in c.get_tugas():
                print(tugas)

        elif choice == "4":
            print("Keluar dari program")
            c.exit()
            break
        else:
            print("liat lagi intruksinya")

if __name__ == "__main__":
    main()