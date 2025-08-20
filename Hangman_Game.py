import random

words = ["apple", "tiger", "chair", "house", "plane"]

word_to_guess = random.choice(words)

guessed_word = ["_"] * len(word_to_guess)

wrong_guesses = 0
max_guesses = 6

guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

while wrong_guesses < max_guesses and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)


    if guess in word_to_guess:
        print("Correct!")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
    else:
        wrong_guesses += 1
        print(f"Wrong guess! You have {max_guesses - wrong_guesses} tries left.")

    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    
if "_" not in guessed_word:
    print("\n You win! The word was:", word_to_guess)
else:
    print("\n Game Over! The word was:", word_to_guess)

