print("Welcome to my computer quiz!")

playing  = input("Do you want to play? ")
# print(playing)

if playing.lower() != "yes":
    quit()
print("Okay! Let's play : )")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random acess memory":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

print("You got " + str(score) + " quesions correct!")
print("You got " + str((score/4)*100) + "%")
