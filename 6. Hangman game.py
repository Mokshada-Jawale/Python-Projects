# Hangman game
import random

def get_word():
    sample_words = 'apple banana kiwi mango pineapple orange grape watermelon cherry papaya peach strawberry'
    sample_words = sample_words.split(' ')
    word = random.choice(sample_words)
    return word

def play_game(word):
        guessing_word = '_'*len(word)
        guessed_letters = []
        guessed_words = []
        tries = len(word) + 5
        guessed = False
        print("Let's start the game! \nHint: Word is a name of a fruit")
        print('You Have ',tries,'Tries to guess the word!')
        print(guessing_word)
        while (guessed != True) and (tries > 0):
            guess = input("Please guess a letter or a word: ").lower()
            if len(guess)==1:
                if guess in guessed_letters:
                    print("You have already guessed the letter",guess)
                    tries -= 1
                elif guess not in word:
                    print(guess," is not in a word")
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("Good job",guess,"is in the word")
                    guessed_letters.append(guess)
                    tries -= 1
                    guessed_words_list = list(guessing_word)
                    indices = []
                    for i, letter in enumerate(word):
                        if letter == guess:
                            indices.append(i)
                    for index in indices:
                        guessed_words_list[index] = guess
                    guessing_word = ''.join(guessed_words_list)
                    print(guessing_word)
                    if '_' not in guessing_word:
                        guessed = True
            elif len(guess) == len(word):
                if guess in guessed_words:
                    print('You have already guessed the word',guess)
                    tries -= 1
                elif guess != word:
                    print(guess,'is not the word.')
                    tries -= 1
                else:
                    guessed = True
                    guessing_word = word
            else:
                print('Your guess is invalid')

        if guessed:
            print('Congratulations!! You guessed the word',word)
        else:
            print('You lost!')
            print('The word was',word)

def main():
    word = get_word()
    play_game(word)
    play_again = input('Do you want to play next round? (Y/N): ')
    while play_again.lower() == 'y':
        word = get_word()
        play_game(word)
        print(play_again)
        break
    else:
        print("That's cool, have a good one!")

if __name__ == '__main__':
    main()
