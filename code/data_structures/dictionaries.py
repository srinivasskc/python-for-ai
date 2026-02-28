empty_dictionary = {}

person = {
    "name" : "Srinivas",
    "age": 34,
    "city": "Bangalore",
    "is_Married" : True
}

person

# Accessing Values by key.
person['age']
person["city"]
person["is_Married"]
person["name"]

person["last_name"] = "kadiyala"
person

person["name"] = "Srinivas"

# Adding new key,value to dictionary
person["license"] = False
person

# Removing key,value from dictionary
del person["license"]
person


# Different way to create dictionary.
# keys must be unique

scores = dict(math=95, science=90, social=75)
scores

# Accessing using get() method.
print(scores.get("math"))
print(scores.get("science","Unknown"))

# Delete items using pop() method.
person

# Removes the is_Married from dict.
person.pop("is_Married")
person

# Removes all items from dict.
person.clear()
person

# Dictionary Methods:

person = {
    "name" : "Srinivas",
    "age": 34,
    "city": "Bangalore",
    "is_Married" : True
}

person

# Get all keys.
person.keys()

# Get all values.
person.values()

# Get all Items
person.items()

# Check key exists.

if "name" in person:
    print(person.get("name"))
else:
    print("name not found")


# Updating multiple values.
person.update({"name": "Srinivas Kadiyala", "age": 35})
person

# Nested Dictionaries.

students = {
    "student_A": {"name": "Srinivas", "roll_no": 1, "grade": "A"},
    "student_B": {"name": "Tejaswini", "roll_no": 2, "grade": "A+"},
    "student_C": {"name": "Raghava", "roll_no": 3, "grade": "O"}   
}

students

# Accessing nested data.
print(students["student_A"]["name"])
print(students["student_C"]["grade"])

# Prints student_A details.
print(students.get("student_A",0))

# Prints zero if not found. Zero is default value.
print(students.get("student_D",0))




