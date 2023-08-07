#Rock Paper Scissors is a game for 2 players. Players simultaneously choose one of the options rock, paper or scissors.
#Rock breaks scissors, scissors cuts paper, paper covers rock. If both players make the same choice, it's a tie.
#Define the choice of the computer itself in your program. Let the player choose one of the three 
#options Rock Paper Scissors and then decide who wins.

player_1 = input("What do you choose: paper, rock or scissors? ")

choice_computer = "paper"

variable_1 = "scissors"
variable_2 = "paper"
variable_3 = "rock"


if player_1 == variable_2 == choice_computer:
    print("You choose paper")
    print("I choose paper")
    print("Its a tie!!")
elif player_1 == variable_3 != choice_computer:
    print("You choose rock")
    print("I choose paper")
    print("Computer wins")
elif player_1 == variable_1 != choice_computer:
    print("You choose scissors")
    print("I choose paper")
    print("You wins :-)")