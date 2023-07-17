a = int(input("Enter your age:"))
print("Your age is : " , a)

if(a>18):
    print("You can Drive")
else:
    print("You cannot ")


price = int(input("Enter Price"))
budjet = int(input("Enter your budjet"))
if (budjet-price > 50):
    print("Everthing is Okay")
elif(budjet-price > 20):
    print("Think about It")
else:
    print("Not Okay")