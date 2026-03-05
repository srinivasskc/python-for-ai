from dotenv import load_dotenv
import os

# Loads the .env file
load_dotenv()

api_key = os.environ.get("API_KEY")

debug = os.environ.get("DEBUG")

database_url = os.environ.get("DATABASE_URL")

print(f"API Key: {api_key}")
print(f"Debug Mode: {debug}")
print(f"Database: {database_url}")
