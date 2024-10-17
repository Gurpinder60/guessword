import random

word_list = ["apple", "banana", "happy", "camel", "dog"]

word = random.choice(word_list)
length = len(word)
lives = 5
game_over = False
correct_letter = []
while not game_over:
    guess_letter = input("Guess Letter:").lower()

    placeholder = ""
    for position in range(length):
        placeholder += "_"

    display = ""
    for letter in word:
        if letter == guess_letter:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)
    if letter not in guess_letter:
        lives -= 1
        if lives == 0:
            print("you Loose")
            game_over = True
    if "_" not in display:
        game_over = True
        print("You win")
print("Start Over")
