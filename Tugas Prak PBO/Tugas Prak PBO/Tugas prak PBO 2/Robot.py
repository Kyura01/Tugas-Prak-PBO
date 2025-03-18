import random

class robot:
    def __init__ (self, nama, hp, attack, akurasi):
        self.nama = nama
        self.attack = attack
        self.hp = hp
        self.akurasi = akurasi
        self.stun = False
        self.stun_duration = 0

    def attack_musuh (self, musuh):
        if random.random() < self.akurasi:
            damage = self.attack
            musuh.hp -= damage
            print(self.nama, "Menyerang ", musuh.nama, "dan menerima ", damage, "damage !")
        else:
            print(self.nama, "Serangan Meleset")

    def regen (self):
        jumlah_heal = random.randint(5,15)
        self.hp += jumlah_heal
        print (self.nama, "Menerima ", jumlah_heal, "HP!")

    def stunned (self,musuh):
        if random.randint(1,100) <= 40:
            musuh.stun = True
            musuh.stun_duration = 2
            print(self.nama, "Stun", musuh.nama, "!")
        else:
            print(musuh.nama, "gagal di stun")

    def update_stun(self):
        if self.stun:
            self.stun_duration -= 1
            if self.stun_duration <= 0:
                self.stun = False
                self.stun_duration = 0
                print(f"{self.nama} terbebas dari stun")

    def is_alive (self):
        return self.hp > 0
    
    def __str__(self):
        return f"{self.nama} [{self.hp} | {self.attack}]"
    
class game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def start(self):
        while self.robot1.is_alive() and self.robot2.is_alive():
            print (f"\nround {self.round} {'=' * 20 }")
            print (self.robot1)
            print (self.robot2) 
            self.player_turn(self.robot1, self.robot2)
            if not self.robot2.is_alive():
                break
            self.player_turn(self.robot2, self.robot1)
            self.round += 1

        if self.robot1.is_alive():
            print("\n ", self.robot1.nama, "menang")
        else:
            print("\n ", self.robot2.nama, "menang")

    
    def player_turn (self, attacker, defender):

        attacker.update_stun()
        defender.update_stun()

        if attacker.stun:
            print (f"{attacker.nama} Terkena stun dan tidak bisa melakukan apapun :( ")
            return
        
        print("\n1. Attack ")
        print("2. Stun")
        print("3. Defend")
        print("4. Heal")
        
        action = input (f"{attacker.nama}, Pilih Langkah anda : ")

        if action == "1":
            attacker.attack_musuh(defender)
        elif action == "2":
            attacker.stunned(defender)
        elif action == "3":
            print(f"{attacker.nama} memillih untuk bertahan")
        elif action == "4":
            attacker.regen()
        else:
            print(f"Pilihan langkah yang anda pilih tidak ada {attacker.nama} tidak melakukan apapun")


robot1 = robot("Vhagar", 150, 13, 0.6)
robot2 = robot("Caraxes", 110, 20, 0.9)

battle = game (robot1, robot2)
battle.start()