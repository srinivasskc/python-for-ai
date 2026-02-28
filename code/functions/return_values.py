# This func only prints the value.
# We cannot use or store the value printed from the function.

def add_print(a,b):
    print(a+b)

add_print(1,2)


# This func returns value.

def add_return(a,b):
    return a + b

sum_result = add_return(5,10)
sum_result
sum_result = sum_result + 10
sum_result

# Calculate the floor area.
def calculate_floor_area(width,height):
    area = width * height
    return area

# store the return value
floor_area = calculate_floor_area(10,8)
print(f"Floor Area: {floor_area} sq.ft")

# Calculate Wall Area
def calculate_wall_area(length,width,height):
    area = 2 * (length + width) * height
    return area

# store the return value
wall_area = calculate_wall_area(12,10,8)
print(f"Wall Area: {wall_area} sq.ft")



# Double example.
def double(number):
    return number * 2

result = double(10)
result

# With expressions.
result = double(10) + double(3)
result

# using conditions
if double(7) > 10:
    print("It's a big number")
else:
    print("Its a small number")

# Passing to another function.
print(double(7))



# Returning multiple values

def simple_function():
    numbers = [1,2,3,4,5,6]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number,last_number

simple_function()
first_number, last_number = simple_function()
print(first_number)
print(last_number)


# Returning min max - tuple.
def get_min_max(nums):
    return min(nums), max(nums)

result_tuple = get_min_max([5, 2, 8, 1, 9])
print(result_tuple)
