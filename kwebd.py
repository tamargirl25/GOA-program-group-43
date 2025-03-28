string_list = ["apple", "banana", "cherry", "date", "elderberry"]
integer_list = [10, 20, 30, 40, 50]
float_list = [1.1, 2.2, 3.3, 4.4, 5.5]
boolean_list = [True, False, True, False, True]
big_list = string_list + [integer_list, float_list, boolean_list]

print(big_list)
# სია არის მონცამეთა ტიპი პითონში, რომელიც იქმენბა კვადრატული ბრჩხილებით - []

# სიაში შეგვიძლია განსხვავებული მონცამეთა ტიპის ელემენტების შენახვა

data = ["Luka", 100, True, 13.5]


# matrix - სია, რომლის ყველა ელემენტები არის სიები ერთი და იგივე ელემენტების რაოდენობით

# square = [
#     [1, 2, 3, 4],
#     [1, 2, 3, 4],
#     [1, 2, 3, 5],
#     [1, 2, 3, 4]
# ]

# print(square[2][3])

# array
# integers = [1, 2, 3]
# floats = [1.5, 2.5, 3.5]
# strings = ["A", "B", "C"]


# indexing არის მეთოდი რომლითაც სიის კონკრეტული ელემენტის წამოღება შეგვიძლია ელემენტის რიგის ნომრით ესეიგი ინდექსით

# indexerror - ეს არის ერორი რომელიც ხდება მაშინ როდესაც ჩვენ ვიყენებთ სიის იმ ინდექს რომელიც სიას არ გააჩნია


# სიის კონკრეტულ ინდექსის მნიშვნელობის განახლება ხდება
# სიის სახელისა და კვადრატულ ბრჩილებში მოცემული ამ ინდექსის
# ახალი მნიშვნელობის მინიჭებით

# data[1] = 50
# print(data)

animals = ["cat", "dog", "bird"]

print(animals[0])

"""1) შექმენით 5 სია, პირველ სიაში შეინახეთ strings, მეორე სიაში integers, მესამეში floats, მეოთხეში booleans (თითოეულ სიაში უნდა იყოს 5 ელემენტი) საბოლოოდ კი შექმენით დიდი სია რომელშიც იქნება ყველა ზევით მყოფ სიაში არსებული ელემენტები. აქედან მხოლოდ strings უნდა იყოს ცალკეულ სიად დიდ სიაში, დანარჩენების კი მხოლოდ ელემენტები გადმოიტანეთ"""

strings = ["Luka", "Tornike", "Barbare", "Giorgi", "Tamar", "Saba"]

integers = [1, 2, 3, 4, 5]
floats = [1.2, 2.2, 3.2, 4.2, 5.2]
booleans = [True, True, False, False, True]

data = [
    ["Luka", "Tornike", "Barbare", "Giorgi", "Tamar", "Saba"], 1, 2, 3, 4, 5, 1.2, 2.2, 3.2, 4.2, 5.2,
    True, True, False, False, True
]

print(data)



#



numbers = [0, 1, 7, 3, 4, 5]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

numbers[2] = numbers[2] *2

print(numbers)
