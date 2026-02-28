# Importing the Whole Module.
import math
math.isqrt(16)

math.sqrt(16)

# Import specific functions from a module.
from math import sqrt,isqrt

sqrt(16)
isqrt(16)

# Random Module
import random

number = random.randint(1,10)
number

choice = random.choice(["Apple","Banana","Grapes"])
choice


# Date and time.
import datetime
today_date_time = datetime.date.today()
today_date_time

today_date = datetime.datetime.now()
today_date



# Operating System
import os
current_working_directory = os.getcwd()
current_working_directory

# JSON
import json
data = {"name": "John", "age": 24}
print(data)
print(type(data))

json_str = json.dumps(data)
print(json_str)
print(type(json_str))


# Import pandas
import pandas as pd
df = pd.DataFrame(data)

# Import Everything
from math import *


"""
Installing packages from terminal

pip install requests
pip install pandas
pip install requests==2.32.5

pip install requests pandas matplotlib numpy

pip list
"""