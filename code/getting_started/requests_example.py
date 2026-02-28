"""
This is my second program
using the import requests
"""


import requests

# Download a web page - Pinging the website.
response = requests.get("https://www.moolya.com/")
print(response.status_code) # Should print 200

