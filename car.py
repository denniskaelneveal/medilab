class Car:
    def __init__(self, color, year):
        self.color = color
        self.year = year

    def drive(self):
        print("you drive a",self.color,"car")

mercedes = Car("red", 2019)
print(mercedes.color)
mercedes.drive()

toyota = Car("yellow", 2020)
print(toyota.color)
toyota.drive()







