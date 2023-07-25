#Write a program that reads the year of birth and then prints whether the user
#is an adult (at least 18 years old) or not. If someone turns 18 this year, 
#you may also consider that person to be an adult.

birth_year = int(input("Enter your year of birth: "))
current_year = int(input("Your age: "))


if current_year < 18:
    print("You're not an adult yet.")
elif current_year == 18:
    print("So you're an adult.")
else:
    print("So you're an adult.")
