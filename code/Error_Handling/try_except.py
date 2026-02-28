# Try the Division by zero, if it fails-go to except block.

try:
    result = 10/0
except:
    print("Hi There!! ")


# Try and Except Clause
try:
    with open('data.txt', 'r') as f:
        content = f.read()
    print("Done!")  # Never reaches here if file missing
except FileNotFoundError:
    print("Could not find the file")


try:
    with open('data.txt', 'r') as f:
        content = f.read()
    number = int(content)
    num = 10/0
except ZeroDivisionError:
    print("Cannot divide number by zero")
except ValueError:
    print("Could not find number in file")
except FileNotFoundError:
    print("File Not Found Error")
    