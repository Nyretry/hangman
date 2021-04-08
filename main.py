from random import randrange
from playsound import playsound


# import pygame


def menu():  # only neaded to make code more neat in main
    print("Welcome to hangman would you like to...\nStart (1)\nExit(2)\nLearn how to play(3)")
    return


# def switchHang (guess,screen):  # this will be fore drawing a the hangman
#     return{
#     1 : pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75),
#     2: 2,
#     3: 'h',
#     4: 2,
#     5: 'h',
#     6: 2,
#     }[guess]

def hangman(word):  # this is where the game of hangman is played
    guess, wrongGuesses = 0, []  # initializes the guess counter and guess attempt log
    progress = list('_' * len(word))  # creates a list of _ for each character
    while guess < 6:  # you have 6 guesses, if you have 0 left then the loop ends
        print(progress)  # Shows your how many letters you have correct
        letter = input(
            "The wrong letters guessed so far are {1}\nYou have {0} guesses left\n>>>Please guess a letter: ".format(
                6 - guess, wrongGuesses)).upper()  # the UI and info needed
        if len(
                letter) == 1 and letter not in wrongGuesses:  # checks to see if its a single character and it hasn't
            # been guessed wrong already. no check for right answer
            if letter in word:  # if the guessed letter is in the word
                for b in range(len(progress)):  # sets up variable b to fill in the progress list
                    if letter == word[b]:  # if the character in the string is the same at index b then
                        progress[b] = letter  # replace the character in the string progress at index b
            else:  # if you guess wrong

                guess += 1  # add guess
                # switchHang(guess,screen)
                wrongGuesses.append(letter)  #


        else:
            print("Only choose one letter")
        if progress == list(word):
            print("Congrats! You win")
            playsound("Old_victory_sound_roblox.mp3")
            return
    print("The correct word was: ", word)
    return


with open('SOWPODS', 'r') as f:
    SOWPODS = f.readlines()
while True:
    word = SOWPODS[randrange(0, len(SOWPODS))]  # gets a random word from the 300k list of words
    word.upper()
    menu()
    x = int(input("Select option: "))
    if x == 2:
        quit()  # quits program if user selects option 2
    if x == 3:
        print("How to play...\nPress enter when ready")
        input()  # just a something to make program sleep while the user is reading the rules.
    hangman(word)
