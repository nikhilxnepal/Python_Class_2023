#Write a program that allows a user to convert the results of a vote into percentages.
#The user enters the number of Yes votes, the number of No votes and the number of blank votes.
#The program shows the percentage of each type of vote.

how_many_people_voted_yes = int(input("Enter the number of people who vote Yes: "))
how_many_people_voted_no = int(input("Enter the number of people who vote No: "))
how_many_people_voted_blank = int(input("Enter the number of blank vote: "))
total_vote = how_many_people_voted_yes+how_many_people_voted_no+how_many_people_voted_blank

percentage_of_yes_vote = (how_many_people_voted_yes / total_vote) * 100
percentage_of_no_vote = (how_many_people_voted_no / total_vote) * 100
percentage_of_blank_vote = (how_many_people_voted_blank / total_vote) * 100

print("YES: ",percentage_of_yes_vote,"%")
print("NO: ",percentage_of_no_vote,"%")
print("BLANK: ",percentage_of_blank_vote,"%")

