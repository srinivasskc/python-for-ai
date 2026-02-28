# defining the function.

def greet():
    print("Hello!!")
    print("Hello Again!!")

# Calling the function.
greet()


# No Return function.

def no_return():
    pass

no_return()

# Calling function multiple times.
greet()
greet()
greet()

# Function with logic

def check_weather():
    temperature = 16
    if temperature >= 25:
        print("Its Hot!")
    elif temperature >= 30:
        print("Its very hot!!")
    elif temperature >=20:
        print("Its normal")
    else:
        print("Its too cold")

check_weather()

