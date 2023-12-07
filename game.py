# echo "# python" >> README.md
#   git init
#   git add README.md
#   git commit -m "first commit"
#   git branch -M main
#   git remote add origin git@github.com:olegjer/python.git
#   git push -u origin main


import random


def def_figure(figure):
    if figure == "r":
        return "Rock"
    if figure == "p":
        return "Paper"
    if figure == "s":
        return "Scissors"


variants = ['r', 'p', 's']
lost = 0
win = 0

while True:
    computer = random.choice(variants)
    player = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ")

    print(
        f"You chose {def_figure(player)}, the computer chose {def_figure(computer)}.")

    if player == computer:
        print(f"Both players selected {def_figure(player)}. It's a tie!")
    elif (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        print(f"{def_figure(player)} covers {def_figure(computer)}! You win")
        # win = win +1
        win += 1
    else:
        print(f"{def_figure(computer)} covers {def_figure(player)}! You lose")
        lost += 1

    is_game = input('Play again? (y/n): ')
    if is_game == 'n':
        break

print(f"Final Scores: \nComputer: {lost} \nPlayer: {win}")

# elif player == 'p' and computer == 'r':
#     print("player win")
# elif player == 's' and computer == 'p':
#     print("player win")


# Rock smashes Scissors.
# Paper covers Rock.
# Scissors cut Paper.
