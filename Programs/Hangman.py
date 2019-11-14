# cvars:
word = input("What is the word?\n").lower()
guessCount = 6 # how many times they can attempt.
def ll():
    print("-------------------")
    print("Word: " + blankWord)
    print("Past Guesses: " + pastGuesses)
    print("-------------------")
def win():
    print("-------------------")
    print("You Win.")
    print("Word: " + blankWord)
    print("-------------------")
def lose():
    print("-------------------")
    print("You Lose.")
    print("Word: " + word)
    print("-------------------")


# dvars:
blankWord = ""
pastGuesses = ""

# "___" Logic.
for i in range(0,len(word)):
    if word[i] == " ":
        blankWord += " "
    else:
        blankWord += "_"
print(blankWord)


while guessCount > 0 and blankWord != word: # game loop, if you run out of chances 
                                            # or guess the entire word.
    ll()
    guess = input("Choose a letter.\n")
    if guess != "": # Fix empty crash.
        pastGuesses += guess[0] + "  "
        booly = False
        for i in range(0,len(word)):
            if word[i] == guess[0]:
                booly = True
                blankWord = blankWord[0:i] + word[i] + blankWord[i+1:len(blankWord)]
        if not booly:
            guessCount -= 1
# Win/Lose:
if word == blankWord:
    win()
else:
    lose()