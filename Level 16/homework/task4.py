#4
read_pages = 25  # წაკითხული გვერდების რაოდენობა
free_time = True  # ჰქონდა თავისუფალი დრო

productive = read_pages >= 20 and free_time  # True - 20-ზე მეტი წაიკითხა და თავისუფალი დრო ჰქონდა

print("პროდუქტიულობა:", productive)