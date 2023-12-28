import random
box="""
                          |            |
                    1     |     2      |      3
             _____________|____________|_______________
                          |            |
                    4     |      5     |     6
             _____________|____________|_______________
                          |            |
                    7     |      8     |     9
                          |            |
"""
#Toss
print(box)
your_selection=eval(input("type 0 for Heads or 1 for Tails:"))
toss=random.randint(0,1)
#selection of symbol
if your_selection==toss:
    toss_winner=1
    print("you won the toss")
    symbol=eval(input("player 1 chose your sign.Enter 0 for X and 1 for O:"))
elif your_selection!=toss:
    toss_winner=2
    print("you lost the toss")
    symbol=eval(input("Player 2 chose your sign.Enter 0 for X and 1 for O:"))
#Assigning the symbol
if symbol==0 or symbol==1:
    if your_selection==toss:
        if symbol==0:
            player1_symbol="X"
            player2_symbol="O"
        elif symbol==1:
            player1_symbol="O"
            player2_symbol="X"
    elif your_selection!=toss:
        if symbol==0:
            player1_symbol="X"
            player2_symbol="O"
        elif symbol==1:
            player1_symbol="O"
            player2_symbol="X"
else:
    print("you entered an invalid decision")

#printing both players symbol
print("player 1 symbol is",player1_symbol)
print("player 2 symbol is",player2_symbol)
#defining boxes
box1=1
box2=2
box3=3
box4=4
box5=5
box6=6
box7=7
box8=8
box9=9
#game rules for winning
def winning_condition():
    if player1_symbol=="O":
        if box1=="O" and box5=="O" and box9=="O":
            print("player1 won")
        elif box1=="O" and box2=="O" and box3=="O":
            print("player1 won")
        elif box4=="O" and box5=="O" and box6=="O":
            print("player1 won")
        elif box3=="O" and box5=="O" and box7=="O":
            print("player1 won")
        elif box7=="O" and box8=="O" and box9=="O":
            print("player1 won")
        elif box1=="O" and box4=="O" and box7=="O":
            print("player1 won")
        elif box2=="O" and box5=="O" and box8=="O":
            print("player1 won")
        elif box3=="O" and box6=="O" and box9=="O":
            print("player1 won")
        if box1=="X" and box5=="X" and box9=="X":
            print("player2 won")
        elif box1=="X" and box2=="X" and box3=="X":
            print("player2 won")
        elif box4=="X" and box5=="X" and box6=="X":
            print("player2 won")
        elif box3=="X" and box5=="X" and box7=="X":
            print("player2 won")
        elif box7=="X" and box8=="X" and box9=="X":
            print("player2 won")
        elif box1=="X" and box4=="X" and box7=="X":
            print("player2 won")
        elif box2=="X" and box5=="X" and box8=="X":
            print("player2 won")
        elif box3=="X" and box6=="X" and box9=="X":
            print("player2 won")
    if player1_symbol=="X":
        if box1=="O" and box5=="O" and box9=="O":
            print("player2 won")
        elif box1=="O" and box2=="O" and box3=="O":
            print("player2 won")
        elif box4=="O" and box5=="O" and box6=="O":
            print("player2 won")
        elif box3=="O" and box5=="O" and box7=="O":
            print("player2 won")
        elif box7=="O" and box8=="O" and box9=="O":
            print("player2 won")
        elif box1=="O" and box4=="O" and box7=="O":
            print("player2 won")
        elif box2=="O" and box5=="O" and box8=="O":
            print("player2 won")
        elif box3=="O" and box6=="O" and box9=="O":
            print("player2 won")
        if box1=="X" and box5=="X" and box9=="X":
            print("player1 won")
        elif box1=="X" and box2=="X" and box3=="X":
            print("player1 won")
        elif box4=="X" and box5=="X" and box6=="X":
            print("player1 won")
        elif box3=="X" and box5=="X" and box7=="X":
            print("player1 won")
        elif box7=="X" and box8=="X" and box9=="X":
            print("player1 won")
        elif box1=="X" and box4=="X" and box7=="X":
            print("player1 won")
        elif box2=="X" and box5=="X" and box8=="X":
            print("player1 won")
        elif box3=="X" and box6=="X" and box9=="X":
            print("player1 won")
#conditions for filling boxes

#STARTING THE GAMES
if toss_winner==1:
    choice1=eval(input("player 1 enter the box number you want to mark:"))
    if choice1==1:
        if choice1==1 and player1_symbol=="X":
            box=("""
                          |            |
                    X     |     2      |      3
             _____________|____________|_______________
                          |            |
                    4     |      5     |     6
             _____________|____________|_______________
                          |            |
                    7     |      8     |     9
                          |            |
""")
            print(box)
        elif choice1==2 and player1_symbol=="X":
            box=("""
                          |            |
                    1     |     X      |      3
             _____________|____________|_______________
                          |            |
                    4     |      5     |     6
             _____________|____________|_______________
                          |            |
                    7     |      8     |     9
                          |            |
""")
            print(box)
        elif choice1==3 and player1_symbol=="X":
            box=("""
                          |            |
                    1     |     2      |      X
             _____________|____________|_______________
                          |            |
                    4     |      5     |     6
             _____________|____________|_______________
                          |            |
                    7     |      8     |     9
                          |            |
""")
            print(box)
        elif choice1==4 and player1_symbol=="X":
            box=("""
                          |            |
                    1     |     2      |      3
             _____________|____________|_______________
                          |            |
                    X     |      5     |     6
             _____________|____________|_______________
                          |            |
                    7     |      8     |     9
                          |            |
""")
            print(box)
        elif choice1==5 and player1_symbol=="X":
            box=("""
                          |            |
                    1     |     2      |      3
             _____________|____________|_______________
                          |            |
                    4     |      X     |     6
             _____________|____________|_______________
                          |            |
                    7     |      8     |     9
                          |            |
""")
            print(box)
        elif choice1==6 and player1_symbol=="X":
            box=("""
                          |            |
                    1     |     2      |      3
             _____________|____________|_______________
                          |            |
                    4     |      5     |     X
             _____________|____________|_______________
                          |            |
                    7     |      8     |     9
                          |            |
""")
            print(box)
        elif choice1==7 and player1_symbol=="X":
             box=("""
                          |            |
                    1     |     2      |      3
             _____________|____________|_______________
                          |            |
                    4     |      5     |     6
             _____________|____________|_______________
                          |            |
                    X     |      8     |     9
                          |            |
""")
             print(box)
        elif choice1==8 and player1_symbol=="X":
             box=("""
                          |            |
                    1     |     2      |      3
             _____________|____________|_______________
                          |            |
                    4     |      5     |     6
             _____________|____________|_______________
                          |            |
                    7     |      X     |     9
                          |            |
""")
             print(box)

        elif choice1==9 and player1_symbol=="X":
             box=("""
                          |            |
                    1     |     2      |      3
             _____________|____________|_______________
                          |            |
                    4     |      5     |     6
             _____________|____________|_______________
                          |            |
                    7     |      8     |     X
                          |            |
""")
             print(box)

             

        







