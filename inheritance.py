# parent class/super class/ base class
class animal:
    def speak(self):
        print("Animal is speaking")
#  child class/sub class/derived class
class cat(animal):
    def meow(self):
        print("Cat is meowing")
class dog(animal):
    def bark(self):
        print("Dog is barking")

a = animal()

c = cat()
c.speak()
d = dog()
d.speak()


















