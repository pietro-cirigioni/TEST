print("Welcome to Ciri's Casino!")

name = input("Please enter your name: ")

while len(name) < 2:
    print("Please enter a valid name.\n")
    name = input("Please re-enter your name: ")

surname = input("Please enter your surname: ")
while len(surname) < 2:
    print("Please enter a valid surname.\n")
    surname = input("Please re-enter your surname: ")   

age = int(input("Please enter your age: "))
while age < 18:
    print("You must be 18 to play.\n")
    age = int(input("Please re-enter your age: "))
else:
    print(f"Welcome {name} {surname}! \n")



