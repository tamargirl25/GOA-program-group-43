score = int(input("შეიყვანეთ ქულა: "))

if score > 50:
    if score > 75:
        print("A")
    else:
        print("B")
elif score > 25:
    print("C")
else:
    print("D")




for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} - ლუწი")
    else:
        print(f"{i} - კენტი")
