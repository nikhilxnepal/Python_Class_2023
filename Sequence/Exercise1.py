#Write a program that retrieves the user's personal data and then prints the address label.
surname = input("Enter the surname: ")
first_name = input("Enter the First Name: ")
street = input("Enter the street: ")
street_number = int(input("Enter the street number: "))
zip_code = int(input("Enter the zip code: "))
city = input("Enter the city name: ")

print(first_name + " " + surname + "\n" + street + " " + str(street_number) + "\n" + str(zip_code) + " " + city )