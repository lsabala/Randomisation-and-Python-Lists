#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

coinTossResult = random.randint(1,2)

if coinTossResult == 1:
  print("Heads")
elif coinTossResult == 2:
  print("Tails")