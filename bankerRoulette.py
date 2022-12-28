# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
amountOfNames = len(names)

RandomNamePicker = random.randint(0,amountOfNames - 1) 

print(names[RandomNamePicker] + " is going to buy the meal today!")