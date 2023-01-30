class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def bark(self):
        print(f'{self.name} : 멍멍')

    def death(self):
        Doggy.num_of_dogs -= 1

    def get_status():
        return f'태어난 강아지는 {Doggy.birth_of_dogs}마리이며, 현재 남아있는 강아지는 총 {Doggy.num_of_dogs}마리입니다.'

choco = Doggy('초코', 'Maltese')
dubu = Doggy('두부', 'Husky')
daegil = Doggy('대길', 'Greyhound')

daegil.bark()

dubu.death()

print(Doggy.get_status())