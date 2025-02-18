#3
# AND ოპერატორი (ორივე პირობა უნდა იყოს True, რომ შედეგი იყოს True)
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# OR ოპერატორი (მინიმუმ ერთი პირობა უნდა იყოს True, რომ შედეგი იყოს True)
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

# NOT ოპერატორი (აბრუნებს საპირისპირო მნიშვნელობას)
print(not True)        # False
print(not False)       # True

# კომბინირებული მაგალითები (მრავალფეროვანი ვარიანტები)
print(not (True and False))   # True  (True and False -> False, not False -> True)
print(not (False or True))    # False (False or True -> True, not True -> False)
print((True and False) or True)  # True  (True and False -> False, False or True -> True)
print((False or False) and True) # False (False or False -> False, False and True -> False)
print(not (True and True) or False) # False (True and True -> True, not True -> False, False or False -> False)
