#Write a program that prints the larger of two numbers. If the numbers are 
#negative, then you use the opposite number.
#But: if both numbers are divisible by 5, then you have to print the smaller 
#of both numbers. If numbers are equal then the answer is just 0.

first_number = int(input("First number: "))
second_number = int(input("Second number: "))

if first_number < 0:
    first_number = -first_number
if second_number < 0:
    second_number = -second_number

if first_number > second_number and not (first_number % 5 == 0 and second_number % 5 == 0):
    print("The answer for the numbers", first_number, "and", second_number, "=", first_number)
elif second_number > first_number and not (first_number % 5 == 0 and second_number % 5 == 0):
    print("The answer for the numbers", first_number, "and", second_number, "=", second_number)
elif first_number % 5 == 0 and second_number % 5 == 0:
    if first_number < second_number:
        print("The answer for the numbers", first_number, "and", second_number, "=", first_number)
    else:
        print("The answer for the numbers", first_number, "and", second_number, "=", second_number)
elif first_number == second_number:
    print("The answer for the numbers", first_number, "and", second_number, "=", 0)