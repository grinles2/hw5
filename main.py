import random


class Student:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.work = False
        self.girl = False  # девушку не завезли в обнову
        self.glad = 30
        self.progress = 0
        self.alive = True
        self.pet = False
        self.money = 150
        self.home = False
        self.hw = 0

    def to_college(self):
        self.progress += 1
        self.glad -= 10
        self.hw += 2
        self.money -= 10  # на проезд
        print("Ну что же,пора идти в универ")

    def to_relax(self):
        self.glad += 10
        self.progress -= 0.5
        self.money -= 20
        print("Пора отдохнуть")

    def to_work(self):
        print("Деньги нужны")
        self.money += 70
        self.glad -= 5
        self.progress += 2
        self.work = True
        # мы не знаем где работаем может по профессии и поэтому получаем прогресс

    def is_alive(self):
        if self.progress < 0:
            print("Отчислен!")
            self.alive = False
        elif self.glad <= 5:
            print("Тебе к психиологу бро")
            self.alive = False
        elif self.progress > 100:
            print("Вы закончили универ")
            self.alive = False
            self.glad += 50

    def to_find_girl(self):
        self.girl = True
        self.glad += 70
        self.money -= 200
        self.girl = True
        print("Ура я не одинокий волк")

    def to_pet(self):
        print("Купить друга")
        self.money -= 40  # на корм и покупку
        self.glad += 20
        self.progress -= 0.5  # отвлекает от учёбы так как мы хотим вернуться домой к нему
        self.pet = True

    def find_home(self):
        self.money -= 150
        self.glad += 10  # мы больше не бомжи
        self.home = True

    def to_sleep(self):
        self.glad += 5

    def do_hw(self):
        self.hw -= 2
        self.glad -= 10
        self.progress += 10

    def end_of_the_day(self):
        print(f"glad =", {self.glad})
        print(f"progress = {round(self.progress), 2}")

    def live(self, day):
        d = f"Day{day} of {self.name} life"
        # d = "Day 1 of Oleg Life
        print(f"{d:=^50}")
        live_cube = random.randint(1, 8)
        if live_cube == 1:
            self.to_college()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_relax()
        elif live_cube == 4:
            self.do_hw()
        elif live_cube == 5:
            self.to_work()
        elif live_cube == 6:
            self.to_pet()
        elif live_cube == 7:
            self.to_find_girl()
        elif live_cube == 8:
            self.find_home()
        self.end_of_the_day()
        self.is_alive()


Alex = Student("Alex")
for day in range(1, 366):
    if Alex.is_alive == False:
        break
    Alex.live(day)
