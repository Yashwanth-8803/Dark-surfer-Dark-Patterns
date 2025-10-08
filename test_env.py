import os
from dotenv import load_dotenv

load_dotenv()  # Load the .env file

print("Loaded API Key:", os.getenv("GOOGLE_API_KEY"))