class Person:
    def __init__(self, name,gender, age):
        self.name = name
        self.gender = gender
        self.age = age


    def details(self):
           print(self.name,"is a", self.gender, self.age)

teacher = Person("joe", "Male", 20)
teacher.details()
print(teacher.name)
accountant = Person("jerry", "Male", 20)
accountant.details()
print(accountant.name)













