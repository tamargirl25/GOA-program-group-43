languages = ["Python", "Java", "C#", "Go", "Ruby", "PHP", "C++", "Swift", "javaScript", "Perl"]

languages[-1] = "Rust"

print("1-დან 5-ის ჩათვლით: ", languages[0:5])
print("2-დან ბოლომდე: ", languages[1:])
print("4-დან 8-მდე: ", languages[3:8])

print("მეექვსედან ბოლომდე: ", languages[-6:])
print("მეექვსემდე ყველაფერი: ", languages[:-5])
print("მეექვსეს ჩათვლით თავიდან ყველაფერი: ", languages[:6])

print("შებრუნებული სია:", languages[::-1] )
