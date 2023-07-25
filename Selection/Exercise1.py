#Write a program that allows the user to test whether a number is a triple.

number = int(input("Enter a number: "))

if number % 3 == 0:
    print(number, "is a triple")
else:
    print(number, "is not divisible by 3")