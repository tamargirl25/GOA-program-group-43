#2)
# list და string ორივე დალაგებული მიმდევრობებია, რაც ნიშნავს, რომ ელემენტებს აქვთ განსაზღვრული ადგილმდებარეობა (ინდექსი) და შეგვიძლია მივწვდეთ თითოეულ ელემენტს
# ინდექსით.

#3)
#Slicing ნიშნავს მიმდევრობის ნაწილს გამოყოფას, ინდექსების მიხედვით.
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # [1, 2, 3]

#4)
numbers = list(range(1, 21))
print(numbers[4:10])  # ინდექსი 4 = 5  . ინდექსი 9 = 10

#5)
celestial_bodies = ["მზე", "მერკური", "ვენერა", "დედამიწა", "მარსი", "იუპიტერი", "სატურნი", "ურანი", "ნეპტუნი"]
even_indexed = celestial_bodies[0::2]
print(even_indexed)

#6)
numbers = list(range(0, 16))
odd_indexed = numbers[1::2]
print(odd_indexed)

#7)
fullname = "ნიკა კობახიძე"
first_name = fullname[:3]   
last_name = fullname[4:]    

print(first_name) 
print(last_name)   

