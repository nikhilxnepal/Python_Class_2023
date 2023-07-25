#Write a program that allows you to repeat a word on the screen.
#You let the user choose a text and the number of times the text will be repeated

number = int(input("Enter a number: "))
text = input("Enter a text: ")

multiply_text = text * number

print(number, "times your text: ", multiply_text)

