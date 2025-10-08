import os
import subprocess
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Print the API key (first few characters for verification)
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    print(f"API key loaded: {api_key[:5]}...")
else:
    print("API key not found!")

# Run the Streamlit app with the correct environment
subprocess.run(["streamlit", "run", "streamlit_app.py", "--server.port", "8502", "--server.headless", "true"])