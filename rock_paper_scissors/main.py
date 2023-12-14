import random as r

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

player_move = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if player_move != 0 and player_move != 1 and player_move != 2:

    print("Invalid number, player lose :(")

else:
    player = f"{rps[player_move]}"

    print(f"Player:\n{player}")

    computer = rps[r.randint(0, 2)]

    print(f"\n\n\nComputer:\n{computer}")

    if not player == computer:
        if (player == rock and computer == paper) or (player == paper and computer == scissors) or (
                player == scissors and computer == rock):

            print("\n\nComputer Wins!!!!")

        else:

            print("\n\nPlayer Wins!!!!")

    else:

        print("\n\nTie!!!!")
        