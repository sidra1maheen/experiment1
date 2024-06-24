from random import choice 
objects = ["Rock", "Paper","Scissors"]
computer = choice(objects)
rps = input("what will you choose? Rock, Paper, or Scissors?").lower().strip()
if rps == computer:
    print("it is a tie! :p")
if rps == ("rock"):
    if computer == ("scissors"):
        print("yay! you won! :)")
if rps == ("paper"):
   if computer == ("rock"):
        print("yay! you won! :)")
if rps == ("scissors"):
    if computer == ("paper"):
        print("yay! you won! :)")                
if computer ==("scissors"):
    if rps == ("paper"):
        print("Noooooo!! you lost :(")    
if computer ==("paper"):
    if rps == ("rock"):
        print("Noooooo!! you lost :(")
if computer ==("rock"):
    if rps == ("scissors"):
        print("Noooooo!! you lost :(")
print("Thanks for playing!")        