#number guessing game

import random  #to generate random number

def start_game():
    random_number = random.randint(1, 11)
    print('Hello! Welcome to the game')
    player_name = input('Enter your name: ')
    want_to_play = input('hii {}, Would you start the game? Enter("Yes/No") '.format(player_name))
    attempts = 0
    while want_to_play.capitalize() == "Yes":
        if attempts <= 7:
            guess = int(input("Pick a number between 1 to 10 \n"))
            if guess<1 or guess>10:
                raise ValueError("Please choose a number within given range")
            elif guess == random_number:
                print("Congratulations! You got it")
                attempts += 1
                break
            elif guess < random_number:
                print("It's lower")
                attempts += 1
            elif guess > random_number:
                print("It's higher")
                attempts += 1
        else:
            print("Better luck next time :)")
            break
    if want_to_play.capitalize() == "No":
        print("That's cool, have a good one!")

if __name__ == "__main__":
    start_game()

