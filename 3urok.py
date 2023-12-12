import random
class Human:
    def __init__(self, name, home=None, car=None):
        self.name = name
        self.money = 200
        self.enjoyment = 100
        self.home = home
        self.car = car

    def get_home(self, home):
        if home != None:
            print("Продали родину")
        self.home = home
        print("Купили новую родину.(партия недовольна)")

    def get_car(self, car):
        if car != None:
            print(f"Продали КРЕЙСЕР марки {car.marka}")
        self.car = car
        print(f"Купили ВЕРТОЛЁТ марки {car.marka}")

    def work(self):
        print("Пошли работать на заводе(партия довольна)")
        money = random.randint(10, 25)
        print(f"Вы заработали {money} мексиканских песо")
        if money >= 20:
            print(f"За столь большую работу вы получаете аудиенцию с самим Си Цзиньпином!")
        self.money += money
        self.enjoyment -= 5
    def chill(self):
        print("Отдыхаем")
        enjoyment = random.randint(3, 8)
        print(f"Вы отдохнули и чувствуете себя на все {enjoyment} процентов!")
        self.enjoyment += enjoyment

    def shopping(self):
        print("Вы пошли скупиться в магазин за продуктами и не только(партии всё-равно, мягко говоря)")
        money = random.randint(10, 25)
        print(f"Вы потратили {money} мексиканских песо, зато у вас теперь дома есть что покушать(наверное)")
        self.money += money
        self.enjoyment -= 5

    def clean_house(self):
        pass

    def life(self):
        pass

    def is_alive(self):
        pass

    def info(self):
        pass

class Car:
    def __init__(self, marka):
        self.marka = marka
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def passengers_info(self):
        print(f"В {self.marka} ", end = '')
        if self.passengers != []:
            print(f"щас в слоне:")
            for p in self.passengers:
                print(p.name)
        else:
            print("НИКОГО НЕМА ЕСЛИ ЧТО")

class Home:
    def __init__(self):
        self.food = 0
        self.cleanliness_level = 50

human1 = Human("ZELENSKY")
human2 = Human("BAIDEN")
human3 = Human("and many billiards rockets...")
car = Car("Leopard")
car.add_passenger(human1)
car.add_passenger(human2)
car.add_passenger(human3)
car.passengers_info()