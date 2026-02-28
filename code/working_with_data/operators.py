# Arithmetic Operators

#Basic Math
print(10+3)
print(10-3)
print(10*3)
print(10/3)

# Special Operators
print(10**3)  # Power - Exponent
print(10//3) # Floor Division (Rounds Donw)
print(10%3)  # Modulus (Remainder)

# Order of Operations - BODMAS
result = 2 + 3 * 4
print(result)

result1 = (2+3)*4
print(result1)



# Logical Operators.

age = 25
has_license = True

# AND Operator - Both must be true.
can_drive = age >=16 and has_license
print(can_drive) #True


# OR - atleast one must be true.

day = "Saturday"

is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)

# AND and OR
age = 25
has_license = True
has_drunk = True  #not has_drunk = not(True) = False

can_drive = age >=16 and has_license and not has_drunk
print(can_drive)


# Truth Tables

print(True and True)
print(True and False)
print(False and False)
print(False and True)

print(True or True)
print(True or False)
print(False or False)
print(False or True)

print(not True)
print(not False)

# Shortcut assignments

score = 10
score = score + 5 

score += 5

