# add
def add(a, b):
    return a + b
# subract
def sub(a, b):
    return a - b
# multiply
def multiply(a, b):
    return a * b
# divide
def divide(a, b):
    return a / b

print("select operation")
print(1,"add")
print(2,"sub")
print(3,"mul")
print(4,"div")
while True:
    choice = int(input("enter your choice: "))
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            print(add(1, 2))
        elif choice == 2:
            print(sub(1, 2))
        elif choice == 3:
            print(multiply(1, 2))
        elif choice == 4:
            print(divide(1, 2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")




