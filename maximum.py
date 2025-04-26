
def max(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print("Number 1: " +str(num1)+ " is greater")
    elif num2 > num1 and num2 > num3:
        print("Number 2: " +str(num2)+ " is greater")
    else:
        print("Number 3: " +str(num3)+ " is greater")
max(20,33,41)