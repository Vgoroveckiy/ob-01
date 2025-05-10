class Warrior:
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать.")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать.")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьет кого то.")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет.")

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Сила: {self.power}")
        print(f"Выносливость: {self.endurance}")
        print(f"Цвет волос: {self.hair_color}")


warrior1 = Warrior("Иван", 10, 15, "черный")
warrior2 = Warrior("Алексей", 12, 14, "русый")
warrior3 = Warrior("Дмитрий", 11, 16, "каштановый")

warriors = [warrior1, warrior2, warrior3]

for warrior in warriors:
    warrior.info()
    warrior.sleep()
    warrior.eat()
    warrior.hit()
    warrior.walk()
    warrior.info()
