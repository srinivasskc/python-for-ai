# empty list
my_list = []

# list with items
age = 34
has_license = True
my_list = ["Alice", 25, age, has_license, False, 21.5, 'c']

# Getting List Items
name = my_list[0]
age = my_list[2]

temperature = my_list[-2]

# Slicing
print(len(my_list))

print(my_list[0:5]) # start from 0 index to (5-1) index
print(my_list[1:]) # start from 1 index to end.

# Changing lists. - Lists are mutable.

my_list[0] = "Srinivas"
my_list

# Appending adds at end.
my_list.append("Kadiyala")
my_list


# Remove will remove by value from list
my_list.remove("Kadiyala")
my_list

# Insert at position.
my_list.insert(1,"Kadiyala")
my_list

# Remove and Return Last Value
last = my_list.pop()
last
my_list

# Remove by index.
del my_list[2]
my_list

# List Methods.
numbers = [3,1,4,1,5,9]

print(numbers)
print(len(numbers)) # length
print(numbers.count(1)) # count recurrences
print(numbers.index(4)) #position of number from list

# Sorting
numbers.sort()
numbers

# Reverse
numbers.reverse()
numbers

# Copy from one list to another
my_new_list = numbers.copy()
my_new_list
numbers

# Checking lists.
fruits = ["Banana", "Apple", "Orange"]

# Check if item exists

if "Apple" in fruits:
    print("Found Apple!")


# Checking if list is empty or not.
if fruits:
    print("List has items")
else:
    print("List is empty")
    


