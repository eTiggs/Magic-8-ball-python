#Modules
import random

# Name
name = ("")
input("what is your name?")

# Question
question = ("")
question = input("What is the question?")

# Answer
answer = ("")

# Number Gen
random_num = random.randint(1, 20)
#print(random_num)

# Control Flow

# Positive
if random_num == 1:
  answer = "Yes - definitely."
elif random_num == 2:
  answer = "It is decidedly so."
elif random_num == 3:
  answer = "It is certain."
elif random_num == 4:
  answer = "Without a doubt."
elif random_num == 5:
  answer = "You may rely on it."
elif random_num == 6:
  answer = "As I see it, yes."
elif random_num == 7:
  answer = "Most likely."
elif random_num == 8:
  answer = "Outlook good."
elif random_num == 9:
  answer = "Yes."
elif random_num == 10:
  answer = "Signs point to yes."
  
# Neutral
elif random_num == 11:
  answer = "Reply hazy, try again."
elif random_num == 12:
  answer = "Ask again later."
elif random_num == 13:
  answer = "Better not tell you now."
elif random_num == 14:
  answer = "Cannot predict now."
elif random_num == 15:
  answer = "Concentrate and ask again."
  
# Negative
elif random_num == 16:
  answer = "My sources say no."
elif random_num == 17:
  answer = "Outlook not so good."
elif random_num == 18:
  answer = "Very doubtful."
elif random_num == 19:
  answer = "Don't count on it."
elif random_num == 20:
  answer = "My reply is no."
  
else:
  answer = "Error"

# Printing
if name == "":
  print("Question:", question)
else:
  print(name, "asks:", question)

print("Magic 8-Balls answer:", answer)
