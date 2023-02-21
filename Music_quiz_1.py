print("Welcome to my music quiz!")

playing = input("Do you want to play? ")

if playing.lower()!= "yes":
    quit()

print("Okay! Lets play :)")
score = 0

answer = input("What year was Roberta Flack born? ")
if answer.lower() == "1937":
    print("Correct!")
    score += 1
else:
    print("INCORRECT!!")

answer = input("Who sings 'Protect Ya Neck? ' ")
if answer.lower() == "wu-tang clan":
    print("Correct!")
    score += 1
else:
    print("lol no.")

answer = input("Which classical composer was Nina Simone influenced by? ")
if answer.lower() == "bach":
    print("Correct!")
    score += 1
else:
    print("INCORRECT!!")

answer = input("Who made the album 'good kid, m.a.a.d city'? ")
if answer.lower() == "kendrick lamar":
    print("Correct!")
    score += 1 
else:
    print("lol no.")

answer = input("Who is the mother of soul music? ")
if answer.lower() == "aretha franklin":
    print("Correct!")
    score += 1
else:
    print("INCORRECT!!")

print('you got ' + str (score) + " questions correct!")
print('you scored ' + str((score/5)* 100) + "%.")





