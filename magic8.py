name ="Philip"
question = "Will I win the lottery?"
answer= ""

#Generate random values to ensure that "answer is different each time program is executed"
import random
# generate a random number between 1 and 9
random_number = random.randint(1,10)
print(random_number)


#Control flow using if/elif/else statements
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
    answer = "Signs point to yes"
else:
  answer = "Error"

#Print the result
if name =="":
  print("Question:", question)
else:
  print (name,"asks:", question)
print("Magic 8-ball's answer:", answer)
