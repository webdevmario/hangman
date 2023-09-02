import random
from os import system

from hangman_art import logo, stages
from hangman_words import word_list

system("clear")
print(logo)

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
solution = []
lives = 6

for letter in chosen_word:
    solution.append("_")

print(stages[lives])

while "_" in solution and lives > 0:
    guess = input("Please select a letter: ").lower()

    system("clear")

    match = False
    existing_word = False

    if guess in chosen_word and guess in solution:
        print("\nYou already guessed that letter.")

        existing_word = True

    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            solution[i] = guess
            match = True

            if not existing_word:
                print(f"Great, {guess} is in the word!")

    if not match:
        lives -= 1

        print(f"Sorry, {guess} is not in the word.\n")

    print(stages[lives])
    print(f"\n{' '.join(solution)}\n")

if lives > 0:
    print("You won!")
else:
    print(f"You lost! The word was: {chosen_word}")
