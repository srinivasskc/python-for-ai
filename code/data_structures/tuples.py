# Empty Tuple.

empty_tuple = ()

# Tuple with Items.
point = (3,5)

coordinates = (12.974658,77.743996)
coordinates

# Without Parenthesis: Implicit
coordinates = 5,10
coordinates

# Single Tuple
single = (42,)
print(single)
print(type(single))


# Without comma, it thinks just a number
no_comma = (42)
print(no_comma)
print(type(no_comma))

# Multiple Values

colors = ("Green","Blue", "Red")
colors

colors[0]

# Re-assigning new value at 0 index.
# colors[0] = "White"
# Tuples are immutable - cannot be changed once declared

# Accessing Items
colors
colors[0]
colors[-1]

# slicing
colors[0:1]
colors[0:]

# Tuple unpacking
coordinates = (12.974658,77.743996)
latitude,longitute = coordinates
print(latitude)
print(longitute)

# Multiple assignment
a,b,c = 1,2,3
print(a)
print(b)
print(c)

# swap variables
longitute,latitude = latitude,longitute
print(latitude)
print(longitute)
