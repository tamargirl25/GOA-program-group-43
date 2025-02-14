# წიგნების თავდაპირველი ფასები
book_price_1 = 30
book_price_2 = 25
book_price_3 = 40
book_price_4 = 50
book_price_5 = 35

# ფასდაკლების ოდენობა (10%)
discount = 10 / 100  # ფასდაკლება პროცენტში

# ახალი ფასები ფასდაკლების გათვალისწინებით
new_book_price_1 = book_price_1 - (book_price_1 * discount)
new_book_price_2 = book_price_2 - (book_price_2 * discount)
new_book_price_3 = book_price_3 - (book_price_3 * discount)
new_book_price_4 = book_price_4 - (book_price_4 * discount)
new_book_price_5 = book_price_5 - (book_price_5 * discount)

# ახალი ფასების დაბეჭდვა
print("ფასდაკლების შემდეგ წიგნების ფასები:")
print("წიგნი 1:", new_book_price_1)
print("წიგნი 2:", new_book_price_2)
print("წიგნი 3:", new_book_price_3)
print("წიგნი 4:", new_book_price_4)
print("წიგნი 5:", new_book_price_5)
