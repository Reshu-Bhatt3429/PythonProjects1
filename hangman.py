import random


word_list = ["cat", "dog", "python", "hangman", "challenge"]
word = random.choice(word_list).lower()
guessed_letters = set()
lives = 6

print("Welcome to Hangman!")
print(f"The word has {len(word)} letters. Try to guess it!")

while lives > 0:

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word.strip())


    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations! You guessed the word: {word}")
        break


    users_guess = input("Guess a letter: ").lower()


    if len(users_guess) != 1 or not users_guess.isalpha():
        print("Invalid input. Please enter a single alphabetical character.")
        continue

    # Check if the letter has already been guessed
    if users_guess in guessed_letters:
        print("You already guessed that letter.")
        continue


    guessed_letters.add(users_guess)


    if users_guess in word:
        print("Good guess!")
    else:
        print("Wrong guess! You lose a life.")
        lives -= 1
        print(f"Lives remaining: {lives}")


if lives == 0:
    print(f"You ran out of lives! The word was: {word}")