#1
fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]
print(fruits[2])  

#2
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25  
print(numbers)

#3
colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]

index = int(input("შეიყვანეთ ინდექსი (0-4): "))

print(colors[index]) 

#4
animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]
animals[-1] = "გემი"

print(animals) 

#5
colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]

index = int(input("შეიყვანეთ ინდექსი (0-3): "))
new_color = input("შეიყვანეთ ახალი ფერი: ")

colors[index] = new_color

print(colors)

