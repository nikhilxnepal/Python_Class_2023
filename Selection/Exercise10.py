#rite a program to determine whether two integers are both OK or not.
#They are OK if
#• they are both between 30 and 40 (inclusive)
#• they are both equal to one of the following numbers: 65, 72, 83, 90.

first_number = int(input("First number: "))
second_number = int(input("Second number: "))

condition_numbers = (65,72,83,90)

if 30 <= first_number <= 40 and 30 <= second_number <= 40:
    print("Both numbers are ok")
elif first_number == second_number == condition_numbers:
    print("Both numbers are ok")
elif not 30 <= first_number == second_number <= 40:
    print("They are NOT ok")
else:
    print("They are NOT ok")