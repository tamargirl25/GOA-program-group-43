#6
score = int(input("შეიტანეთ თქვენი ქულა: "))  # მომხმარებლის ქულა

if score > 80:
    grade = "A"
elif score > 60:
    grade = "B"
elif score > 40:
    grade = "C"
elif score > 20:
    grade = "D"
else:
    grade = "F"

print(f"თქვენი შეფასება: {grade}")  # ქულის მიხედვით შეფასების დაბეჭდვა
