class Ninja:
    def __init__(self, first_name, treats, pet_food,):
        self.name = first_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet('Bark Ruffalo', 'Shiba Inu', 'flip')
    
    def walk(self):
        self.pet.play()
        print('WALKING WITH BARK RUFFALO')
    def feed(self):
        self.pet.eat()
        print('BARK RUFFALO IS EATING')
    def bathe(self):
        self.pet.noise()
        print('YOU ARE BATHING BARK RUFFALO')
class Pet:
    def __init__(self, name, dogtype, tricks):
        self.name = name
        self.type = dogtype
        self.tricks = tricks
        self.health = 20
        self.energy = 50
    
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5 
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print('ARRRFFF!')

matt = Ninja('Matt', 'Bully Bites', 'Cheerios')
matt.walk()
matt.bathe()
matt.feed()