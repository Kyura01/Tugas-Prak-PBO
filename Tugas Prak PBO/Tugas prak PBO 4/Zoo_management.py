from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, name, jenis):
        self.__name = name
        self.__jenis = jenis 

    @abstractmethod
    def sound(self):
        pass

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_jenis(self):  
        return self.__jenis

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "cat")

    def sound(self):
        return "Meow"
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "dog") 

    def sound(self):
        return "Guk guk"
    
class Trex(Animal):
    def __init__(self, name):
        super().__init__(name, "trex")

    def sound(self):
        return "Rawrrr"
    

def add_animal():
    try:
        name = input("Masukan nama hewan : ")
        if not name:
            raise ValueError("Kasih nama ke hewannya")
        
        jenis = input("Masukan jenis hewan (cat/dog/trex) : ").lower()
        if jenis == "cat":
            return Cat(name)
        elif jenis == "dog":
            return Dog(name)
        elif jenis == "trex":
            return Trex(name)
        else:
            raise ValueError("Jenis hewan tidak ditemukan")
        
    except ValueError as e:
        print(f"Error: {e}")
        return None
    
def main():
    animals = []        

    while True:
        print("\nMenu")
        print("1. Add animal")
        print("2. List animal")
        print("3. Exit")
        choice = input("Masukan pilihan : ")

        if choice == "1":
            new_animal = add_animal()  # Hindari shadowing variable 'animal'
            if new_animal:
                animals.append(new_animal)

        elif choice == "2":
            for animal in animals:
                print(f"Nama: {animal.get_name()}, Jenis: {animal.get_jenis()}, Suara: {animal.sound()}")

        elif choice == "3":
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi")

if __name__ == "__main__":
    main()