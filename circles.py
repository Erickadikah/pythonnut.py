import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f'psst, the chosen solution is {chosen_word}.')

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
display = []
for _ in range(word_length):
    display += "-"

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # check guesssed letter.
    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

    if "-" not in display:
        end_of_game = True
        print("you win.")