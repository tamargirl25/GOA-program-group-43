#3
#for ციკლი
sum_of_numbers = 0  # ცვლადი, რომელშიც შევინახავთ ჯამს

for i in range(1, 16):  # რიცხვები 1-დან 15-მდე
    sum_of_numbers += i  # ვამატებთ თითოეულ რიცხვს ჯამში

print(sum_of_numbers)  # დაბეჭდეთ ჯამი

#while ციკლი
sum_of_numbers = 0  # ცვლადი, რომელშიც შევინახავთ ჯამს
i = 1

while i <= 15:  # სანამ i ნაკლებია ან თანაბარია 15-ს
    sum_of_numbers += i  # ვამატებთ i-ს ჯამში
    i += 1  # ვზრდით i-ს

print(sum_of_numbers)  # დაბეჭდეთ ჯამი
