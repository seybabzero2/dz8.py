import random
import logging

logging.basicConfig(level = logging.DEBUG,
                    filename = "logs.log",
                    filemode = "a",
                    format = "We have next logging message:%(asctime)s:%(levelname)s - %(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 0
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("UCHITSA")
        logging.info("Учеба ")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("Отдохнуть бы конечно не помешало")
        logging.info("Отдых ")
        self.gladness +=3
    def to_chill(self):
        logging.info("Чил ")
        print("Три в ряд")
        self.gladness += 5
        self.progress -= 0.1
    def is_alive(self):
        if (self.progress < -0.5):
            logging.warning("Смерть")
            print("YOU DIED!")
            self.alive = False
        elif self.gladness <= 0:
            logging.warning("Депрессия")
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            logging.warning("Екстерн")
            print("Extern")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day: " + str(day) + " of " + self.name + " suffering"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
nick = Student(name = "Anatolii")
for day in range(9999):
    if nick.alive == False:
        break
    nick.live(day)