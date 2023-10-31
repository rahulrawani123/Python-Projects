// In this program we have created a Rock Paper Scissors game in which the user can play this game with the computer.

import random 
i=1
countuser=0
countcomputer=0
while(i<=3):
    print("\nRound ",i,"\n")
    print("Enter 0 for Rock, \n 1 for Paper, \n 2 for Scissor ")
    user = int(input("Enter Your Choice :- "))
    if(user==0):
        print("You have choosen Rock ")
    elif(user==1):
        print("You have choosen Paper ")
    elif(user==2):
        print("You have choosen Scissors")

    if user>=3 or user<0:
        print("You have choosen wrong Choice ... Try again ..")
    else:
        bot = random.randint(0,2)
        
        if(bot==0):
            print("Computer have choosen Rock ")
        elif(bot==1):
            print("Computer have choosen Paper ")
        elif(bot==2):
            print("Computer have choosen Scissors")
            
        if(user==bot):
            print("Its a Tie ..")
            countuser+=1
            countcomputer+=1
      
        elif(user==0 and bot==2):
            print("You Won ...")
            countuser+=1
        elif(user==2 and bot==0):
            print("Computer won ...")
            countcomputer+=1   
        elif(bot>user):
            print("Computer won ...")
            countcomputer+=1
        elif(user>bot):
            print("You won ...")
            countuser+=1
    i+=1

print("\n")
print("GAME SCORECARD ---------- ")   
print("Your wins = ",countuser)
print("Computer wins = ",countcomputer)
if(countuser==countcomputer):
          print("\n--------------Its a Tie....--------------- ")
elif(countcomputer>countuser):
     print("\n---------Computer win...-------------")
else:
     print("\n----------------You win..-------------")
