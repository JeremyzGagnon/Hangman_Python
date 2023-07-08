import random, string
def main():
    # Word list for the game
    listOfWords = ["python", "java", "swift", "javascript"]
    winCount = 0
    lossCount = 0
    # Selecting a word
    secretWord = random.choice(listOfWords)

    # Game menu
    while(True):
        playersChoice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ').lower()
        if playersChoice == "play":
            if hangmanGame(secretWord):
                winCount += 1
                print(winCount)
            else:
                lossCount += 1
        elif playersChoice == "results":
            print(f"You won: {winCount} times.")
            print(f"You lost: {lossCount} times.")
        elif playersChoice == "exit":
            break
        else:
            continue
# The main game
def hangmanGame(secretWord):
    usersAttempt = 8
    usersPastGuess = []
    lowercase_letters = [char for char in string.ascii_lowercase]

    # print("H A N G M A N")
    print("")
    secretWordReveal = ["-" for _ in secretWord]
    # TODO only letters restriction
    while usersAttempt != 0 and secretWordReveal.__contains__("-"):

        #Check if user input does not contain more than one letter and the letter is not uppercase or not a valid letter
        while(True):
            print("".join(secretWordReveal))
            usersGuess = input("Input a letter: ")
            if len(usersGuess) > 1 or len(usersGuess) == 0:
                print("Please, input a single letter.")
                print("")
                continue
            if any(char.isupper() for char in usersGuess) or usersGuess not in lowercase_letters:
                print("Please, enter a lowercase letter from the English alphabet.")
                print("")
                continue
            break


        # Check if the user tried that guess before
        if usersPastGuess.__contains__(usersGuess):
            print("You've already guessed this letter.")
            # usersAttempt -= 1
            continue
        # Reveal the characters in the secretWordReveal
        if usersGuess in secretWord:
            for index, char in enumerate(secretWord):
                if char == usersGuess:
                    secretWordReveal[index] = usersGuess
        else:
            print("That letter doesn't appear in the word.")
            print("")
            usersAttempt -= 1

        usersPastGuess.append(usersGuess)
        print("")

    if usersAttempt != 0:
        print(f"You guessed the word {secretWord}!")
        print("You survived!")
        return True
    else:
        print("You lost!")



if __name__ == '__main__':
    main()
