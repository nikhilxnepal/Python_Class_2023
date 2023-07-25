#Write a program that allows the user to search for the smallest of 3 numbers.

first_number = int(input("Number 1: "))
second_number = int(input("Number 2: "))
third_number = int(input("Number 3: "))

smallest_number = min(first_number, second_number, third_number)

print("The smallest number is ", smallest_number)