#5
correct_pin = "1234"  # სწორი PIN კოდი
attempts = 3  # მცდელობების მაქსიმალური რაოდენობა

while attempts > 0:
    user_pin = input("შეიტანეთ PIN კოდი: ")  # მომხმარებლის მიერ შეყვანილი PIN
    
    if user_pin == correct_pin:
        print("Access Granted")  # თუ PIN სწორი არის
        break  # გასვლა ციკლიდან
    else:
        attempts -= 1  # მცდელობების შემცირება
        if attempts > 0:
            print(f"არასწორი PIN. დარჩენილი მცდელობები: {attempts}")
        else:
            print("Access Denied")  # თუ მცდელობები ამოწურულია
