#2
number = int(input("შეიტანეთ რიცხვი: "))  # მომხმარებლის მიერ შეყვანილი რიცხვი

if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
