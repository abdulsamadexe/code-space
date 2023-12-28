import random
a="1"
b="2"
c="3"
d="4"
e="5"
f="6"
g="7"
h="8"
i="9"
grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
print(grid)
name1=input("player 1 enter your name")
name2=input("plaer 2 enter your name")
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
print(f"{name1} symbol is",player1_symbol)
print(f"{name2} symbol is",player2_symbol)
#game rules for winning
winning_conditi0n=True
def winning_condition():
    if player1_symbol=="O":
        if a=="O" and e=="O" and i=="O":
            print("player1 won")
            winning_conditi0n=False
        elif a=="O" and b=="O" and c=="O":
            print("player1 won")
            winning_conditi0n=False
        elif d=="O" and e=="O" and f=="O":
            print("player1 won")
            winning_conditi0n=False
        elif c=="O" and e=="O" and g=="O":
            print("player1 won")
            winning_conditi0n=False
        elif g=="O" and h=="O" and i=="O":
            print("player1 won")
            winning_conditi0n=False
        elif a=="O" and d=="O" and g=="O":
            print("player1 won")
            winning_conditi0n=False
        elif b=="O" and e=="O" and h=="O":
            print("player1 won")
            winning_conditi0n=False
        elif c=="O" and f=="O" and i=="O":
            print("player1 won")
            winning_conditi0n=False
        elif a=="X" and e=="X" and i=="X":
            print("player2 won")
            winning_conditi0n=False
        elif a=="X" and b=="X" and c=="X":
            print("player2 won")
            winning_conditi0n=False
        elif d=="X" and e=="X" and f=="X":
            print("player2 won")
            winning_conditi0n=False
        elif c=="X" and e=="X" and g=="X":
            print("player2 won")
            winning_conditi0n=False
        elif g=="X" and h=="X" and i=="X":
            print("player2 won")
            winning_conditi0n=False
        elif a=="X" and d=="X" and g=="X":
            print("player2 won")
            winning_conditi0n=False
        elif b=="X" and e=="X" and h=="X":
            print("player2 won")
            winning_conditi0n=False
        elif c=="X" and f=="X" and i=="X":
            print("player2 won")
            winning_conditi0n=False
    if player1_symbol=="X":
        if a=="O" and e=="O" and i=="O":
            print("player2 won")
            winning_conditi0n=False
        elif a=="O" and b=="O" and c=="O":
            print("player2 won")
            winning_conditi0n=False
        elif d=="O" and e=="O" and f=="O":
            print("player2 won")
            winning_conditi0n=False
        elif c=="O" and e=="O" and g=="O":
            print("player2 won")
            winning_conditi0n=False
        elif g=="O" and h=="O" and i=="O":
            print("player2 won")
            winning_conditi0n=False
        elif a=="O" and d=="O" and g=="O":
            print("player2 won")
            winning_conditi0n=False
        elif b=="O" and e=="O" and h=="O":
            print("player2 won")
            winning_conditi0n=False
        elif c=="O" and f=="O" and i=="O":
            print("player2 won")
            winning_conditi0n=False
        if a=="X" and e=="X" and i=="X":
            print("player1 won")
            winning_conditi0n=False
        elif a=="X" and b=="X" and c=="X":
            print("player1 won")
            winning_conditi0n=False
        elif d=="X" and e=="X" and f=="X":
            print("player1 won")
            winning_conditi0n=False
        elif c=="X" and e=="X" and g=="X":
            print("player1 won")
            winning_conditi0n=False
        elif g=="X" and h=="X" and i=="X":
            print("player1 won")
            winning_conditi0n=False
        elif a=="X" and d=="X" and g=="X":
            print("player1 won")
            winning_conditi0n=False
        elif b=="X" and e=="X" and h=="X":
            print("player1 won")
            winning_conditi0n=False
        elif c=="X" and f=="X" and i=="X":
            print("player1 won")
            winning_conditi0n=False

grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
while winning_conditi0n==True:
    if toss_winner==1:
        choice1=eval(input("player 1 enter the box number you want to mark:"))
        if choice1=="X" or choice1=="O":
            print("invalid decision")
            print(f"{name1} loses")
            winning_conditi0n=False
        elif choice1==1:
            a=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==2:
            b=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==3:
            c=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==4:
            d=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==5:
            e=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==6:
            f=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==7:
            g=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==8:
            h=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==9:
            i=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        winning_condition()
        choice2=eval(input("player 2 enter the box you want to mark:"))
    if winning_conditi0n==True:

        if choice2==1:
            a=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==2:
            b=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==3:
            c=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==4:
            d=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==5:
            e=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==6:
            f=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==7:
            g=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==8:
            h=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==9:
            i=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        print(grid)
    winning_condition()
    if winning_conditi0n==True:
        
    elif toss_winner==2:
        choice1=eval(input("player 1 enter the box number you want to mark:"))
        if choice1==1:
            a=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==2:
            b=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==3:
            c=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==4:
            d=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==5:
            e=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==6:
            f=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==7:
            g=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==8:
            h=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        elif choice1==9:
            i=player2_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
        choice2=eval(input("player 2 enter the box you want to mark:"))
        if choice2==1:
            a=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==2:
            b=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==3:
            c=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==4:
            d=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==5:
            e=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==6:
            f=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==7:
            g=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==8:
            h=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        elif choice2==9:
            i=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
        print(grid)
    winning_condition()
    