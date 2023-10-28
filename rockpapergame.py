// In this program we have created a Rock Paper Scissors game in which the user can play this game with the computer.

import random 
print("Enter 1 for Rock, \n 2 for Paper, \n 3 for Scissor ")
user = int(input("Enter Your Choice :- "))
print("Your choice :- ",user)
if user>=3 or user<0:
    print("You have choosen wrong Choice ... Try again ..")
else:
    bot = random.randint(0,2)
    print("Computer choice :- ",bot) 
    if(user==bot):
        print("Its a Tie.... ")
    elif(user==0 and bot==2):
        print("You Won")
    elif(user==2 and bot==0):
        print("Computer Wins..")    
    elif(bot>user):
        print("Computer Wins.. ")
    elif(user>bot):
        print("You Won.. ")

