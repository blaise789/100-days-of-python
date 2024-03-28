import  random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
while True:
 player=None
 while player not in choices:
  player=input("rock,paper,or scissors?:").lower()
  if player==computer:
      print("Tie")
      print("computer:",computer,"player:",player)
  elif player=="rock":
      if computer=="paper":
          print("you lose")
          print("computer:",computer,"player:",player)

      else:
        print("you win")
        print("computer:",computer,"player:",player)

  elif player=="paper":
      if computer=="rock":
          print("you win")
          print("computer:",computer,"player:",player)
      else:
        print("you lose")
        print("computer:",computer,"player:",player)

  elif player=="scissors":
      if computer=="rock":
          print("you lose")
          print("computer:",computer,"player:",player)

      else:
        print("you win")
        print("computer:",computer,"player:",player)
 player_choice=input(" do you want to play again (yes/no)?:")
 if(player_choice!='yes'):
      print('bye')
      break
