#Write a program that allows you to judge whether a party is stupid, 
#good or fantastic.
#This depends on the number of bottles of wine and the number of pizzas.
#- The party is good if there are at least 5 pizzas and 5 bottles of wine
#- The party is fantastic if on top of that the number of pizzas is double the number of bottles of
#wine (or vice versa)
#- Otherwise, it's a stupid party.

no_of_wine_bottles = int(input("How many bottles of wine are there: "))
no_of_pizzas = int(input("How many pizzas are there: "))

if no_of_pizzas >= 5 and no_of_wine_bottles >= 5:
    if no_of_pizzas == 2 * no_of_wine_bottles or no_of_wine_bottles == 2 * no_of_pizzas:
        print("This is a good party")
    else:
        print("This is a fantastic party")
else:
    print("This is just a stupid party")