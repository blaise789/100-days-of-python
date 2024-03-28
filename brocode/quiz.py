def new_game():
    guesses=[]
    correct_guesses=0
    quest_no=1
    for key in questions:
        print("----------------------")
        print(key)
        for i in options[quest_no-1]:
          print(" ",i)
        guess=input("enter the correct choice")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses+=check_answer(questions.get(key),guess)
        quest_no += 1
    display_score(correct_guesses,guesses)
def check_answer(answer,guess):
 if answer==guess:
     print("CORRECT")
     return 1
 else:
     print("Wrong!")
     return  0
def display_score(correct_guesses,guesses):
    print("----------")
    print("Results")
    print("correct answers:",end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("your answers are:",end=" ")
    for key in guesses:
        print(key,end=" ")
    score=int((correct_guesses/len(questions))*100)
    print()
    print("your marks are"+str(score)+"%")
def play_again():
    feedback=input("would you like to play again(yes,no)?")
    feedback.upper()
    if feedback=="YES":
        return True
    else:
        return False
questions={
    "who created python":"A",
    "what year was python created":"B",
    "Python is tributed to which comedy group?":"C",
    "Is Kigali the capital city of Rwanda?":"B"
}

options=[
    ["A. Guido van Rossum","B. Elon Musk","C. Bill Gate","D. Steve jobs"],
    ["A. 1989","B,1991","C. 2000","D. 2015"],
    ["A.Lonely island","B. Smosh","C. Monty Python","D. SNL"],
    ["A. Burundi","B.Kigali","C.Kampala","D.Cape Town"]
]
new_game()
while play_again():
    new_game()