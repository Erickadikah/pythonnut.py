import random

word_list = ["baboon", "elephant", "monkey", "lamar", "camel"]
# using random for the choice to be randon.
chosen_word = random.choice(word_list)

print(f'the chosen solution is {chosen_word}')
# this prints randomly chosen word and assign it to a variable called chosen_word.
#chosen_word = random.choice(word_list)

display = []
for _ in range(word_lenth):
    display += "-"
# asking the user to guess a letter and assign their answer to a variable called guess. in lower case
end_of_game = False
while not end_of_game:
  guess = input("Guess a letter: ").lower()
# check if the letter guessed by the user is one of the  chosen_word.
for latter in range(word_lenth):
    letter = chosen_word[position]
    print(f"Current position: {position}\n current letters: {letter}\n guessed letter : {guess}")
    display[position] = letter
    print(display)

    if "-" not in display:
        end_of_game = True
        print("you win")

# loop through each position in the chosen_word.
# if letter at position matches "guess" raeveal letter in the diplayat position.


# prints "display" and you should see the guessed letter in the correct position
# and any other repl NB dont worry about getting the user to guess the next letter

for position in range(word_lenth):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter


print(display)