name = "Srinivas K"
age = 34

string = "Hello, my name is srinivas."

# f-string
string_formatted = f"Hello, my name is {name}"

intro = f"Hello, my name is {name}. I am {age} years old."


# String Methods.

text = "Python for AI - Full Beginner Course, Youtube by Dave Ebbelaar"
print(text.lower())  # converts to lowercase
print(text.upper())  # converts to uppercase
print(text.title())  # converts to Title case.


# Cleaning Strings.

# Removing leading and trailing spaces
spaces = "   Hello, World   "
print(spaces)
print(spaces.strip())

# Removing the character from the string
price = "$19.33"
print(price)
print(price.strip('$'))

cost = "19.33rs"
print(cost)
print(cost.strip('rs'))


# Finding and Replacing
message = "I love Python programming with Python"

# Check if exists
print("Python" in message)
print(message.startswith("I"))
print(message.endswith("Python"))

# Find Position
print(len(message))
print(message.find("Python")) #First Occurence 31
print(message.count("Python")) #Count no of times it appeared

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)
