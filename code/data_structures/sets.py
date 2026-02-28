# Empty Set
empty_set = ()
empty_set

# Set with Values.
numbers = {1,2,3,4,5,6}
numbers
type(numbers)


# Set with array list
fruits = set(["Banana","Grapes","Watermelon"])
fruits
type(fruits)

# Lists -> remove duplicates via sets.
scores = [85,0,0,0,19,20]
unique_scores = set(scores)
unique_scores

# Adding item
colors = {"Orange","White","Green"}
colors.add("Blue")
colors

# Removing Items
colors.remove("Yellow") #Key not found.
colors.discard("Yellow") #Key ignored if not found
colors.discard("Blue")
colors

# Membership testing - Check if exists.
if "Green" in colors:
    print("Green is in colors")
else:
    print("Color Not Found")


# List -> Set -> List
names = ["Raghava","Srinivas","Raghava","Kadiyala"]
unique_names = list(set(names))
unique_names

# Fast Membership testing with sets.
allowed_users = {"Srinivas","Raghava","Tejaswini"}

if "Srinivas" in allowed_users:
    print("Access Granted")
