import os
import subprocess
import sys

# Set the working directory
api_dir = r"c:\Users\jukan\Downloads\OneDrive_2025-04-29\DARK PATTERNS1\Dark-Patterns\api"
os.chdir(api_dir)

# Run the Streamlit app
streamlit_app_path = os.path.join(api_dir, "simple_streamlit_app.py")
print(f"Running Streamlit app: {streamlit_app_path}")
subprocess.run(["streamlit", "run", streamlit_app_path, "--server.port", "8502", "--server.headless", "true"])