import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child:
    def __init__(self, father, mother):
        self.father_blood_type = father.blood_type
        self.mother_blood_type = mother.blood_type
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        if self.father_blood_type == "A" and self.mother_blood_type == "A":
            return "A"
        elif self.father_blood_type == "A" and self.mother_blood_type == "O":
            random_blood_type = ["A", "O"]
            return random.choice(random_blood_type)
        elif self.father_blood_type == "O" and self.mother_blood_type == "A":
            random_blood_type = ["A", "O"]
            return random.choice(random_blood_type)
        elif self.father_blood_type == "A" and self.mother_blood_type == "B":
            random_blood_type = ["A", "B", "AB"]
            return random.choice(random_blood_type)
        elif self.father_blood_type == "B" and self.mother_blood_type == "A":
            random_blood_type = ["A", "B", "AB"]
            return random.choice(random_blood_type)
        elif self.father_blood_type == "B" and self.mother_blood_type == "B":
            return "B"
        elif self.father_blood_type == "B" and self.mother_blood_type == "O":           
            random_blood_type = ["B", "O"]
            return random.choice(random_blood_type)
        elif self.father_blood_type == "O" and self.mother_blood_type == "B":           
            random_blood_type = ["B", "O"]
            return random.choice(random_blood_type)
        elif self.father_blood_type == "O" and self.mother_blood_type == "O":
            return "O"
        else:
            return "Darah alien"

father = input ("Masukkan golongan darah ayah : ")
mother = input ("Masukkan golongan darah ibu : ")
father = Father(father)
mother = Mother(mother)

determining_blood_type = Child(father, mother)
print ("anak memiliki golongan darah : ", determining_blood_type.blood_type)
