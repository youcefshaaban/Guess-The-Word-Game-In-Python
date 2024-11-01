# Guess The Word Game 

## Wanted To Test My Abilities In Loops Especially In While Loop

```python
# So You Can See The Source Code But I'll Put Here To Copy It Quickly And Play With Your Friends

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
```
# Requirments
- just Download Python From [Python Org](https://python.org)
- Also You Need To Have A Compiler Or Just Click On The File To Open It

Check If Python Works Or Not

```bash
python --version
```

if it's Give You This Message

```bash
python 3.13.0
```
