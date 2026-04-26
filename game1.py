import random
while True:
    choice= ["rock","paper","scissor"]
    computer=random.choice(choice)
    player=None
    while player not in choice:
        player=input("enter your choice(rock,paper,scissor): ")
    if player==computer:
        print("computer: ",computer)
        print("player: ",player)
        print("tie")
    elif player=="rock":
        if computer=="paper":
             print("computer: ",computer)
             print("player: ",player)
             print("you loose")
        if computer=="scissor":
             print("computer: ",computer)
             print("player: ",player)
             print("you win")     
    elif player=="paper":
        if computer=="scissor":
             print("computer: ",computer)
             print("player: ",player)
             print("you loose")
        if computer=="rock":
             print("computer: ",computer)
             print("player: ",player)
             print("you win")   
    elif player=="scissor":
        if computer=="rock":
             print("computer: ",computer)
             print("player: ",player)
             print("you loose")
        if computer=="paper":
             print("computer: ",computer)
             print("player: ",player)
             print("you win")
    play_again=input("you want to play again(yes,no): ")
    if play_again !=" yes":
         break
            
