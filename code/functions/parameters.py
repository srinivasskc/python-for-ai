# defining the function with parameters.

def greet(name):
    print(f"Hello, {name}")
    print(f"Hello Again!!, {name}")

# Calling the function.
greet('Srinivas')
greet('Kadiyala')


# Multiple Parameters
def greet_explicit(first_name, last_name):
    print(f"Hello, {first_name}, {last_name}")

# Explicit calling
greet_explicit(first_name="Srinivas", last_name="Kadiyala")
greet_explicit(last_name="Kadiyala",first_name="Srinivas")

# functions with default parameters.
def default_value(first_name="Srini"):
    print(f"Hello {first_name}")

default_value()

# functions with default parameters.
def default_firstname(last_name, first_name="Srini"):
    print(f"Hello {first_name}, {last_name}")

default_firstname(last_name="kadiyala")

# functions with default parameters.
def default_both_names(first_name="Srinivas",last_name="Kadiyala"):
    print(f"Hello {first_name}, {last_name}")

default_both_names()

# Override the default value.
# functions with default parameters.
def default_override_names(first_name="Srinivas",last_name="Kadiyala"):
    print(f"Hello {first_name}, {last_name}")

default_override_names(first_name="Vasishta")

# Calculating the tax and total.

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total Price: ${final_price}")

# order matters
calculate_total(100,0.1,10)
calculate_total(price=100, tax_rate=0.1, discount=10)



# Local Variables.

def calculate_price(price):
    # Default Values.
    tax_rate = 0.1
    discount = 10
    tax = price * tax_rate
    total_price = price + tax - discount
    print(f"Total: ${total_price}")

calculate_price(100)

# We cant call the variable created inside the function, outside.
# print(tax_rate)
# NameError: name 'tax_rate' is not defined


# Global Variables
discount = 10

def calculate_cost(price):
    # Default Values.
    tax_rate = 0.1
    discount=20
    tax = price * tax_rate
    total_price = price + tax - discount
    print(f"Total: ${total_price}")

calculate_cost(100)

print(discount)


# Modifying Global Variables
# If we want to modify the global variable,
# Then we need to first declare global for variable name.
# TIP: Avoid using global when possible and use values as parameters and return results.

counter = 0 # Global Variable

def increment():
    global counter
    counter = counter+1

increment()
increment()
increment()
print(counter)


# Default values - List

def add_list_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list

add_list_item("Banana")
add_list_item("Apple")
add_list_item("Grapes")



