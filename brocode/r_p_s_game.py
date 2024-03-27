import  random
choices=["rock","paper","scissors"]
computer=random.choice(choices)
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

