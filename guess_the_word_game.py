word = "Python"
guesses = 5
userGuess = input("Guess The Word: ").strip().capitalize()

while userGuess != word and guesses > 1:
    guesses -= 1
    print("Wrong!!")
    print(f"You Have {guesses} Guesses Left!")
    userGuess = input("Try Again").strip().capitalize()

    if guesses == 0:
        print("You Have Ran Out Of Guesses :(")
        break

else:
    print("You Have Guess The Word Correctly!! ;)")
