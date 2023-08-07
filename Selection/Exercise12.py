#The scouts divide their members into groups they call sections. On the basis of age, the scouts are divided into 4 groups.
#• Boys/girls from 6 to 7 (included) are Beavers
#• Boys/girls from 8 to 10 (included) are Cubs.
#• Boys/girls from 11 to 13 (included) are Scouts.
#• Boys/girls from 14 to 18 (included) are Explorers.
#• Boys/girls 18 older than 18 are assumed to be Leaders.
#Create a program that asks for your age and uses it to determine the scouts section.

your_age = int(input("Your age = "))

if your_age < 6:
    print("You're too young!")
elif 6 == your_age == 7:
    print("You'll be assigned to the Beavers")
elif 8 <= your_age <= 10:
    print("You'll be assigned to the Cubs")
elif 11 <= your_age <= 13:
    print("You'll be assigned to the Scouts")
elif 14 <= your_age <= 18:
    print("You'll be assigned to the Cubs")
else:
    print("You'll be assigned to the Leaders")
    