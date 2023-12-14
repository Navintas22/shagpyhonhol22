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
        self.home.food -= 2

    def chill(self):
        print("Отдыхаем")
        enjoyment = random.randint(3, 8)
        print(f"Вы отдохнули и чувствуете себя на все {enjoyment} процентов!")
        self.enjoyment += enjoyment

    def shopping(self):
        print("Вы пошли скупиться в магазин за продуктами и не только(партии всё-равно, мягко говоря)")
        money = random.randint(3, 10)
        enjoyment = random.randint(5, 15)
        foodyha = random.randint(5, 10)
        print(f"Вы потратили {money} мексиканских песо, зато у вас теперь дома есть что покушать(наверное)")
        self.money -= money
        self.enjoyment += enjoyment
        self.home.food += foodyha

    def clean_house(self):
        if Home != None:
            print("Дом купи")
        else:
            print("Вы чистите дом(партия одобряет).")
            musor = random.randint(3, 8)
            enjoyment = random.randint(5, 10)
            cleanliness_level = random.randint(10, 15)
            print(f"Вы почистили дом и убрали {musor}кг мусора!")
            self.enjoyment -= enjoyment
            self.home.cleanliness_level -= cleanliness_level

    def life(self):
        self.work()
        r = random.randint(1, 4)
        if r == 1:
            self.work()
        elif r == 2:
            self.chill()
        elif r == 3:
            self.clean_house()
        else:
            self.shopping()


    def is_alive(self):
        if self.money <= 0 or self.home.food <= 0:
            print("смэрть.")
            return False
        return True

    def info(self):
        print("—————————————————")
        print(f"Стан персонажа {self.name}:")
        print(f"====Рiвень задоволення====: {self.enjoyment}")
        print(f"======Залишок грошей======: {self.money}")
        print(f"======Кiлькiсть iжi=======: {self.home.food}")
        print(f"====Порядок в кiмнатi=====: {self.home.cleanliness_level}")

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
        self.food = 50
        self.cleanliness_level = 50

human = Human("ZELENSKY", car=Car("Leopard"), home=Home())
day = 1
while(human.is_alive()):
    print()
    print(f"День {day}")
    human.life()
    human.info()
    day += 1

'''car = Car("LEOPARD")
car.add_passenger(human)
car.passengers_info()'''