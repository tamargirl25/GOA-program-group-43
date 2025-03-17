#7
sentence = input("შეიტანეთ წინადადება: ")  # მომხმარებლის წინადადება

vowels = "aeiouAEIOU"  # ხმოვნები (პატარაობაც და დიდი ასოებიც)
vowel_count = 0  # ხმოვნების რაოდენობა
consonant_count = 0  # თანხმოვნების რაოდენობა

for char in sentence:  # ვ遍ტო თითოეულ სიმბოლოზე წინადადებაში
    if char.isalpha():  # მხოლოდ ასოებზე მუშაობა
        if char in vowels:
            vowel_count += 1  # თუ ხმოვანია, გაზრდი ხმოვნების რაოდენობა
        else:
            consonant_count += 1  # თუ არა, მაშინ ეს არის თანხმოვანი

print(f"ხმოვნების რაოდენობა: {vowel_count}")
print(f"თანხმოვნების რაოდენობა: {consonant_count}")
