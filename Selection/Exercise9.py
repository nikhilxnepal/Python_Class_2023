#Write a program that helps you calculate the number of degrees Fahrenheit (Tf) when you enter the temperature in degrees Celsius (Tc). Use this conversion formula between Tc and Tf :

degree_celsius = float(input("Enter the number of degrees Celsius: "))

degrees_fahrenheit = (degree_celsius * 9/5) + 32

print(degree_celsius, "degrees Celsius = ", degrees_fahrenheit, "degrees Fahrenheit")