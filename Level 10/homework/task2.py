#2
user_input = input("შეიყვანეთ მნიშვნელობა: ")

if user_input.isdigit():
    value = int(user_input)
elif user_input.replace('.', '', 1).isdigit() and user_input.count('.') < 2:
    value = float(user_input)
else:
    value = user_input

print(f"შეყვანილი მნიშვნელობაა: {value}, ტიპი: {type(value)}")

