import random
print("Magic 8 ball")
que=str(input("Ask any question: "))
ball=random.randint(1,8)
if ball == 1:
 print("Yes - definitely.")
if ball == 2:
 print("It is decidedly so.")
elif ball == 3:
 print("Without a doubt.")
elif ball == 4:
 print("Reply hazy, try again.")
elif ball == 5:
 print("Ask again later.")
elif ball == 6:
 print("Better not tell you now.")
elif ball == 7:
 print("My sources say no.")
elif ball == 8:
 print("Outlook not so good.")
elif ball == 9:
 print("Very doubtful.")