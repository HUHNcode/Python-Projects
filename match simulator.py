import random


hobbys = ["Schwimmen", "Lesen", "Malen", "Tanzen", "Kochen"]
interests = ["Programmierung", "Grafikdesign", "Naturwissenschaften", "Technologie", "Musik"]
ages = ["25", "40", "60", "70"]
genders = ["weiblich", "männlich"]
nationalities = ["Deutsch", "Französisch", "Spanisch", "Italienisch", "Japanisch"]

class Students:

    def __init__(self):
        self.hobby = random.choice(hobbys)
        self.interest = random.choice(interests)
        self.age = random.choice(ages)
        self.gender = random.choice(genders)
        self.nationality = random.choice(nationalities)

        self.attributes_list = [self.hobby, self.interest, self.age, self.gender, self.nationality]
for i in range(10):
    exec(f'student{i} = Students()')

print(student2.attributes_list)
print(student3.attributes_list)
geminsam = set(student2.attributes_list) & set(student3.attributes_list)
while True:
    counter = 0
    while True:
        counter += 1
        x = Students()
        y = Students()
        print(x.attributes_list)
        print(y.attributes_list)
        geminsam = set(x.attributes_list) & set(y.attributes_list)
        if len(geminsam) >= 4:# cange the value hera 
            print(counter)
            break
    
    if counter >= 200: # cange the value hera
        break

