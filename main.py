import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# Choose a random word from the list
secret_word = random.choice(word_list)
word_length = len(secret_word)
attempts = 6
guessed_letters = []

# Function to display the current state of the word
def display_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
name = input("your name->")
print("Welcome to Wordle!"+name)
print(f"The secret word has {word_length} letters. You have {attempts} attempts.")

while attempts > 0:
    print("\nCurrent word:", display_word())
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
        if display_word() == secret_word:
            print("Congratulations! You've guessed the word:"+name, secret_word)
            break
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left."+name)

if attempts == 0:
    print("Out of attempts. The secret word was:"+name, secret_word)




