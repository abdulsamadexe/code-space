import random
print('''
 _  _               _                                         _                                       _ 
 | \| | _  _  _ __  | |__  ___  _ _   __ _  _  _  ___  ___ ___(_) _ _   __ _   __ _  __ _  _ __   ___ | |
 | .` || || || '  \ | '_ \/ -_)| '_| / _` || || |/ -_)(_-<(_-<| || ' \ / _` | / _` |/ _` || '  \ / -_)|_|
 |_|\_| \_,_||_|_|_||_.__/\___||_|   \__, | \_,_|\___|/__//__/|_||_||_|\__, | \__, |\__,_||_|_|_|\___|(_)
                                     |___/                             |___/  |___/                      
''')
def difficulty_level():
  global difficulty
  global attempt
  difficulty=input("select difficulty level.Type \"easy\" or \"hard\" :: ").lower()
  while difficulty!="easy" and difficulty!="hard":
      print("Please enter a valid choice")
      difficulty=input("select difficulty level.Type \"easy\" or \"hard\"").lower()
  if difficulty=="easy":
      attempt=10
  elif difficulty=="hard":
      attempt=5
  

def easy_level(number):
    global attempt
    attempts=attempt
    while attempts!=0:
      print(f"you have {attempts} attempts remaining to guess the number")
      guess=int(input("Make a guess :: "))
      if guess<number:
          print("attempts is too low")
          attempts-=1
      elif guess>number:
          print("attempts is too high")
          attempts-=1
      elif guess==number:
          print(f"You got it! The answer was {number}")
          break
    if attempts==0:
        print(f'You ran out of guesses. The correct answer was {number}')


def hard_level(number):
    global attempt
    attempts=attempt
    while attempts!=0:
      print(f"you have {attempts} attempts remaining to guess the number")
      guess=int(input("Make a guess :: "))
      if guess<number:
          print("attempts is too low")
          attempts-=1
      elif guess>number:
          print("attempts is too high")
          attempts-=1
      elif guess==number:
          print(f"You got it! The answer was {number}")
          break
    if attempts==0:
        print(f'You ran out of guesses. The correct answer was {number}')
while True:
  number=random.randint(1,100)
  difficulty_level()
  
  print("I am guessing a number between 1 to 100 ")

    
  if difficulty=="easy":
      easy_level(number)
  elif difficulty=="hard":
      hard_level(number)
  repeat=input("Do you want to play again?\"Yes\" or \"No\"").lower()
  if repeat=="no":
      print("Thank you for playing the game")
      break
      

