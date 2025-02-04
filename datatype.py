number = 20 #Int
num = 34.78 #Float
greeting = "Hello there" #String
Ispythoninteresting = True #Boolean
# Data structures
cars = ["Honda", "Porsche", "Subaru"] #list
fruits = ("banana", "apple") #tuple
countries = {"kenya","England","Italy","India"}
details = {
    "Firstname" : "John",
    "course" : "MIT",
    "Nationality" : "US",
    "age" : 19
} #Dictionary - key-value pair




print(number,num,greeting,Ispythoninteresting)
print(cars,fruits,countries,details)
print(details["Nationality"])
#Determining the data type
print(type(greeting))
print(type(countries))

#typecasting-converting one datatype to another
print(float(number))
