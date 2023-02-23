# Rock, Paper or scissor game

import random

print('Rules for the Rock, Paper or Scissor game are: \n'
      'Rock v/s Paper .... Paper wins \n'
      'Rock v/s Scissor .... Rock wins \n'
      'Paper v/s Scissor .... Scissor wins')
def start_game():
    want_to_play = input("Would you like to start the game? Enter(Yes/No): ")
    while want_to_play.capitalize() == "Yes":
        print("Enter your choice \n"
              "1 for Rock \n"
              "2 for Paper \n"
              "3 for Scissor \n")
        user_input = int(input("Your turn: "))
        if user_input in (1,2,3):
            if user_input == 1:
                user_choice = "Rock"
            elif user_input == 2:
                user_choice = "Paper"
            else:
                user_choice = "Scissor"
            print('You choose: {}'.format(user_choice))
            print("Now, It's computer turn..")
            computer_input = random.randint(1,3)
            if computer_input == 1:
                computer_choice = "Rock"
            elif computer_input == 2:
                computer_choice = "paper"
            else:
                computer_choice = "Scissor"
            print('Computer choose: {}'.format(computer_choice))
            if user_input == computer_input:
                print("Both of you select {}, So it's a tie!".format(user_input))
                break
            elif user_input == 1:
                if computer_input == 2:
                    print("Paper covers rock! You lose.")
                else:
                    print("Rock smashes scissors! You win!")
            elif user_input == 2:
                if computer_input == 1:
                    print("Paper covers rock! You win!")
                else:
                    print("Scissors cuts paper! You lose.")
            elif user_input == 3:
                if computer_input == 1:
                    print("Rock smashes scissors! You lose.")
                else:
                    print("Scissors cuts paper! You win!")
            next_round = input("Do you want to play next round? Enter(Yes/No): ")
            if next_round.capitalize() == "No":
                print("That's cool, Have a good one!")
                break
        else:
            print("Invalid choice, Please try again")
    if want_to_play.capitalize() == "No":
        print("That's cool, Have a good one!")

if __name__ == "__main__":
    start_game()