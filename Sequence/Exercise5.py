#Write a program to convert an amount in Euro into Dollar. 
#You first have to read the current exchange rate.

exchange_dollar_rate = float(input("Enter the current exchange dollar rate (€ -> $): "))
amount_in_euro = float(input("Enter your amount in euro: "))
exchanged_rate = amount_in_euro * exchange_dollar_rate

print(amount_in_euro, '€', "=" , exchanged_rate, "$")