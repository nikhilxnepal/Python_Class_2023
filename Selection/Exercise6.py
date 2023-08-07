#Write a program in which you declare three boolean variables (is_morning, is_mother, is_asleep)
#that you also give a value.

#Then write the code to decide if you need to answer your mobile phone, according to these rules:
#• You normally answer your phone except in the morning, then you only answer if it's your mother.
#• When you're asleep, you never answer the call.
#Test your program by changing the three variables a number of times!

#Individual variable declarations
is_morning = True
is_mother = True
is_asleep = False

if is_asleep == False:
    if is_morning and not is_mother:
        print("I'm not answering my phone")
else:
    print("You should answer your phone")
