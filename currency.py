print("\n!...Welcome to Currency Converter...!")
print(".\n.\n.\n.\n.\nPress any key to continue..")
try:
    import msvcrt
    msvcrt.getch()
except ImportError:
    input()
print("\n!..Choose any one from the below option..!")       
print("\n1. India")
print("2. Euro")
print("3. Pesos")
print("3. Soles")
print("3. Reais")
currency= str(input("\n What currency you want to convert in USD? : "))
if currency == "India" or currency=="1":
    money=float(input(" Enter amount in Rupees: "))
    usd= money*0.012
    print("You have total $ ", usd)
elif currency=="Euro" or currency =="2":
     money=float(input(" Enter amount in Euros: "))
     usd = money * 1.08
     print("You have total $", usd)
elif currency == "Pesos" or currency=="3":
    money = float(input(" Enter amount in Pesos: "))
    usd = money * 0.059
    print("You have total $", usd)
elif currency == "Soles" or currency=="4":
    money = float(input(" Enter amount in Soles: "))
    usd = money * 0.27
    print("You have total $", usd)
elif currency == "Reais" or currency=="5":
    money = float(input(" Enter amount in Reais: "))
    usd = money * 0.20
    print("You have total $", usd)
else:
    print("Currency not recognized.")
     