#Read in three numbers a, b, and c, all equal to 0, 1, or 2.
#Now determine the test result and print it out.

#• If the three numbers are equal to 2, then the result is 10. If all 
#three are equal but not equal to 2 then the result is 5.
#• In the other case: if the numbers b and c are different from a then 
#the result is 1. In all other cases the result is 0.

a = int(input("number 1 (0, 1, or 2): "))
b = int(input("number 2 (0, 1, or 2): "))
c = int(input("number 3 (0, 1, or 2): "))

if a == b == c == 2:
    print(10)
elif a == b == c != 2:
    print(5)
elif b != a and c != a:
    print(1)
else:
    print(0)