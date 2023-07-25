#Write a program that reads a 3-digit number and prints the following information.
#Do not use string functions to find the separate digits.

three_digit_number = int(input("Enter the three-digit number: "))
half = three_digit_number / 2
double =three_digit_number * 2
third_power = three_digit_number ** 3
tenfold = three_digit_number * 10

print("Half: ", half)
print("Double: ", double)
print("Third Power: ", third_power)
print("Tenfold: ", tenfold)

first_digit = three_digit_number // 100
second_digit = (three_digit_number % 100) // 10
three_digit = ( three_digit_number % 100 ) % 10

print("The digits are: ", '\n', first_digit , '\n' , second_digit , '\n' , three_digit )