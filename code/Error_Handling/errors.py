# Syntax Errors

# Missing colon
if x > 5
    print("Big number")


# Runtime Errors.
# Division by zero
result = 10 / 0  # ZeroDivisionError

# Variable doesn't exist
print(score)  # NameError

# Wrong type
"hello" + 5  # TypeError


# This will crash if the file doesn't exist
with open('data.txt', 'r') as f:
    content = f.read()
print("Done!")  # Never reaches here if file missing



