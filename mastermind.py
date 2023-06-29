# Here's the text from the Rules slide
# •There are six colors
# •Computer randomly chooses a secret code (4 colors, can have duplicates, in a specific order)
# •Player has 10 tries to guess the secret code
# •After each guess, computer "grades" the guess, as follows:
# •1 black peg for each exact match (right color in the right spot)
# •1 white peg for each color match (right color in the wrong spot)
import random

colors = ['r', 'g', 'b', 'o', 'p', 'y']

def random_combination():
    secret_code = []
    for i in range(4):
        secret_code.append(random.choice(colors))
    return secret_code
checked = []

def check_guess():
    blacks = 0
    whites = 0
    checked = []
    checked += secret_code
    unchecked_colors = set(checked)
    #print(unchecked_colors)
    for i in range(len(guess_list)):
        if guess_list[i] == secret_code[i]:
            blacks += 1
            checked[i] = 'x'

    for i in range(len(guess_list)):
        if guess_list[i] in checked:    # displays as many whites as there are repeats of a given color (if guessed by the player)
            whites += 1
      # if guess_list[i] in unchecked_colors:  #displays only one white for one color, even if there are repeats
      #      print('white')
      #      unchecked_colors.remove(guess_list[i])

    print('black '*blacks, 'white '*whites)
#    print(checked)




secret_code = random_combination()
#print(secret_code)
x=0
for i in range(11):
    x+=1
    print('theses are the possible colors:', *colors)
    guess_str = input('try {}. provide color a combination:'.format(x))
    if len(guess_str) != 4:
        guess_str = input('provide a combination consisting of 4 letters:')
    guess_list = []
    for i in range(len(guess_str)):
        guess_list += guess_str[i]
    check_guess()
    if secret_code == guess_list:
        print('you win')
        break
    if x == 10:
        print('you lose. the secret combination was:', *secret_code)


