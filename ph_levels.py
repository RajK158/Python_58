# If ph is greater than 7, output "Basic".
# If ph is less than 7, output "Acidic".
# Else, output "Neutral"
ph=int(input("Enter the ph level: "))
if (ph > 7):
    print("Basic level")
elif (ph < 7):
    print("Acidic level")
else:
    print("Neutral level")