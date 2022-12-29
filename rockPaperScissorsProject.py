# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Are you ready to become a champion? Show me what you got\n")
userChoice = int(input('Type "0" for Rock: Type "1" for Paper: Type "2" for Scissors: '))

if userChoice >= 3 or userChoice < 0:
  print("\nWrong answer! Game Over!")
else:
  if userChoice == 0:
    print("\nYou Chose: Rock\n")
    print(rock)
  elif userChoice == 1:
    print("\nYou Chose: Paper\n")
    print(paper)
  elif userChoice == 2:
    print("\nYou Chose: Scissors\n")
    print(scissors)
 
  pcChoice = random.randint(0,2)

  if pcChoice == 0:
    print("Computer Chose: Rock\n")
    print(rock)
  elif pcChoice == 1:
    print("Computer Chose: Paper\n")
    print(paper)
  elif pcChoice == 2:
    print("Computer Chose: Scissors\n")
    print(scissors)

###############################################################
#Wins
  if (userChoice == 0 and pcChoice == 2):
    print("You Win!")
  elif (userChoice == 2 and pcChoice == 1):
    print("You Win!")
  elif (userChoice == 1 and pcChoice == 0):
    print("You Win!")

#Lose
  if (userChoice == 2 and pcChoice == 0):
    print("You Lose!")
  elif (userChoice == 1 and pcChoice == 2):
    print("You Lose!")
  elif (userChoice == 0 and pcChoice == 1):
    print("You Lose!")

#Tie
  if (userChoice == 0 and pcChoice == 0):
    print("Tie!")
  elif (userChoice == 1 and pcChoice == 1):
    print("Tie!")
  elif (userChoice == 2 and pcChoice == 2):
    print("Tie!")
  
#rock(0) wins against scissors(2).
#scissors(2) win against paper(1).
#paper(1) wins against rock(0).


#ALTERNATIVE
'''game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
  print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end'''
  


