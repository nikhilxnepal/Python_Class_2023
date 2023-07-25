#Write a program that allows the user to test if it is possible that one of 
#the three numbers he reads is the sum of the other two numbers.

first_number = int(input("Number 1: "))
second_number = int(input("Number 2: "))
third_number = int(input("Number 3: "))

if first_number == second_number + third_number:
    print("This works")
else:
    print("This won't work")