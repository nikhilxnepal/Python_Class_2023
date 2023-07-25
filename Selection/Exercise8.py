#Write a program that allows a user to know what time his alarm will go off when he indicates what time it is (only the hour is entered) and how long he wants to wait.

current_hour = int(input("Enter the current hour: "))
want_to_wait = int(input("How long do you want to wait: "))

alarm_hour = (current_hour + want_to_wait) % 24

print("The alarm will sound at ", alarm_hour,"h")