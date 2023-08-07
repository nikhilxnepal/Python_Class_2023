#A person's BMI (body mass index) is calculated as follows:
#(weight/length**2) ∗ 10000

#The value of the BMI is decisive to judge the weight of an (adult) person:
#• BMI < 18 underweight
#• 18 <= BMI < 25 normal weight
#• 25 <= BMI < 27 slightly overweight
#• 27 <= BMI < 30 moderate overweight
#• 30 <= BMI < 40 obese
#• 40 >= BMI sickly obese
#Create a program that asks for your weight and height and shows the BMI and the conclusion.

weight_in_kilograms = float(input("Your weight in kilograms: "))
length_in_centimetres = float(input("Your length in centimetres: "))

bmi = (weight_in_kilograms/length_in_centimetres**2) * 10000

print("A person of ", weight_in_kilograms, " kg with a lenfth of ", length_in_centimetres, "cm has a BMI", bmi)

if bmi < 18:
    print("This is a underweight.")
elif 18 <= bmi < 25:
    print("This is a normal weight.")
elif 25 <= bmi < 27:
    print("This is a slightly overweight.")    
elif 27 <= bmi < 30:
    print("This is a moderate overweight.")
elif 30 <= bmi < 40:
    print("This is a obese.")
else:
    print("This is a sicky obese.")
