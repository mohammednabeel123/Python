#Hangman game
print("Welcome to Hangman game. You have 6 attempts. Good luck!!!")

max_attempts = 6
attempts = 0
word = input("Generate a word: ").lower()
guessed_letters = ["_"] * len(word)  # Initialize a list to store guessed letters

while attempts < max_attempts:
    guess = input("Enter a letter: ").lower()

    if guess in word:
        print("Correct guess!")
        
        # Update guessed_letters with the correct guesses
        for i in range(len(word)):
            if word[i] == guess:
                guessed_letters[i] = guess

        print("Current word:", " ".join(guessed_letters))

        # Check if the word is completely guessed
        if "_" not in guessed_letters:
            print("Congratulations! You've guessed the word:", word)
            break

    else:
        attempts += 1
        print("Wrong guess! Attempts left:", max_attempts - attempts)

# Check if the player has run out of attempts
if attempts == max_attempts:
    print("Sorry, you ran out of attempts. The correct word was:", word)
