import os
import sys
import subprocess
import webbrowser
import time

def check_python_installed():
    try:
        subprocess.run([sys.executable, "--version"], check=True, capture_output=True)
        return True
    except:
        print("Python is not installed or not in PATH. Please install Python 3.8 or higher.")
        return False

def install_requirements():
    print("Installing API requirements...")
    requirements_path = os.path.join("api", "requirements.txt")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], check=True)
        print("Requirements installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        return False

def generate_models():
    print("Generating models...")
    generate_models_path = os.path.join("api", "generate_models.py")
    try:
        subprocess.run([sys.executable, generate_models_path], check=True)
        print("Models generated successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error generating models: {e}")
        return False

def start_api_server():
    print("Starting API server...")
    api_path = os.path.join("api", "app.py")
    try:
        # Start the server in a new process
        api_process = subprocess.Popen([sys.executable, api_path])
        print("API server started successfully.")
        return api_process
    except Exception as e:
        print(f"Error starting API server: {e}")
        return None

def open_extension_instructions():
    print("\nTo use the Chrome extension:")
    print("1. Open Chrome and go to chrome://extensions/")
    print("2. Enable 'Developer mode' (toggle in the top-right corner)")
    print("3. Click 'Load unpacked' and select the 'app' folder in this project")
    print("4. The extension should now be installed and ready to use")
    
    choice = input("\nWould you like to open Chrome extensions page now? (y/n): ")
    if choice.lower() == 'y':
        webbrowser.open("chrome://extensions/")

def main():
    # Change to the project directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=== Dark Patterns Detector Deployment ===")
    
    # Check if Python is installed
    if not check_python_installed():
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Generate models
    if not generate_models():
        return
    
    # Start API server
    api_process = start_api_server()
    if not api_process:
        return
    
    # Wait for the server to start
    print("Waiting for the API server to start...")
    time.sleep(3)
    
    # Open extension instructions
    open_extension_instructions()
    
    print("\nPress Ctrl+C to stop the server and exit.")
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping the server...")
        api_process.terminate()
        print("Server stopped. Goodbye!")

if __name__ == "__main__":
    main()