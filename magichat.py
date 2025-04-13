# Write code below 💖

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
dd=int(input("Q1. Do you like Dawn or Dusk?\n1. Dawn\n2. Dusk\n: "))


if dd == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif dd ==2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong Input") 
dead=int(input("Q2. When I’m dead, I want people to remember me as:\n1. The Good \n2. The Great\n3. The Wise \n4. The Bold\n: ")) 
if dead == 1:
  Hufflepuff += 2
elif dead == 2:
  Slytherin += 2
elif dead == 3:
  Ravenclaw += 2
elif dead == 4:
  Gryffindor += 2
else:
  print("Wrong Input") 
please=int(input("Q3. Which kind of instrument most pleases your ear? \n1. The violin \n2. The trumpet \n3. The piano \n4. The drum\n: "))
if please == 2:
  Hufflepuff += 4
elif please == 1:
  Slytherin += 4
elif please == 3:
  Ravenclaw += 4
elif Please == 4:
  Gryffindor += 4
else:
  print("Wrong Input") 
print("Slytherin " +str(Slytherin))
print("Gryffindor "+str(Gryffindor))
print("Hufflepuff "+str(Hufflepuff))
print("Ravenclaw "+str(Ravenclaw))