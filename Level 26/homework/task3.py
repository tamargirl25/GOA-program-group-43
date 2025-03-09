#4
# მომხმარებლისგან ორ რიცხვს ვიღებთ
start = int(input("შეიტანეთ პირველი რიცხვი: "))
end = int(input("შეიტანეთ მეორე რიცხვი: "))

# ვსაზღვრავთ რიცხვებს უმცირესიდან უდიდესამდე
if start > end:
    start, end = end, start

# ცვლადი, რომელშიც დავიმახსოვრებთ ჯამს
sum_of_numbers = 0

# for ციკლი, რათა გამოვავლინოთ რიცხვები start-დან end-მდე
for i in range(start, end + 1):
    sum_of_numbers += i

# დაბეჭდეთ ჯამი
print(f"ჯამი არის: {sum_of_numbers}")
