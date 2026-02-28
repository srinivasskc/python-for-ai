
# if-else
temperature = 25

if temperature > 25:
    print("It's Hot")
else:
    print("It's Nice Weather")


# if-elif-else:
temperature = 31

if temperature > 30:
    print("It's Very Hot")
elif temperature > 25:
    print("It's Hot")
else:
    print("It's Nice Weather")


# if-elif-elif-else:

score = 85
if score >= 90:
    print("A: Excellent")
elif score >=80 and score <90:
    print("B: Good Job!")
elif score >= 70 and score <80:
    print("C: Keep it up!")
else:
    print("D: Needs Improvement")

# Another example.

age = 25
has_license = True
has_drunk = True

if age >=16 and has_license and not has_drunk:
    print("You can drive!")
else:
    print("You cannot drive!")


# Nested Conditions:
has_ticket = False
movie_certificate = "A"
age = 16

if has_ticket:
    if movie_certificate == "U/A":
        if age >=18:
            print("Enjoy the Movie!")
        else:
            print("Needs Supervision by a Parent")
    elif movie_certificate == "A":
        if age >=18:
            print("Enjoy the Movie!!!")
        else:
            print("You are not allowed to watch the movie!")
else:
    print("Please buy the ticket")
