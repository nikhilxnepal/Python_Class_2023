#Create a program that calculates how much you have to pay. 
#First the customer has to enter his data (power consumption is always a whole number).

power_consumption_during_day = int(input("Power consumption during the day (kilowatt per hour): "))
power_consumption_at_night = int(input("Power consumption at night (kilowatt per hour): "))
print("Invoice")
print("*******")

fix_annual_charge = float(83.6)
day_consumption = power_consumption_during_day * 0.068
night_consumption = power_consumption_at_night * 0.035

total_consumption = day_consumption + night_consumption
total_consumption_excluding_vat = total_consumption + fix_annual_charge
total_consumption_including_vat = total_consumption_excluding_vat + ((total_consumption_excluding_vat/100)*21)

print("Fixed costs: €", fix_annual_charge)
print("Daily consumption: €", day_consumption)
print("Night consumption: €", night_consumption)
print("Total excluding VAT: €", total_consumption_excluding_vat)
print("Total including VAT: €", total_consumption_including_vat)