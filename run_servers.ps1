# PowerShell script to run both the Flask API server and the Streamlit app

# Function to run a command in a new PowerShell window
function Start-ProcessInNewWindow {
    param (
        [string]$WorkingDirectory,
        [string]$Command
    )
    
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$WorkingDirectory'; $Command"
}

# Set the working directory
$apiDir = "c:/Users/jukan/Downloads/OneDrive_2025-04-29/DARK PATTERNS1/Dark-Patterns/api"

# Start the Flask API server in a new window
Write-Host "Starting Flask API server..."
Start-ProcessInNewWindow -WorkingDirectory $apiDir -Command "python app.py"

# Wait a moment to ensure the first window opens
Start-Sleep -Seconds 2

# Start the Streamlit app in a new window
Write-Host "Starting Streamlit app..."
$streamlitAppPath = Join-Path -Path $apiDir -ChildPath "simple_streamlit_app.py"
Start-ProcessInNewWindow -WorkingDirectory $apiDir -Command "streamlit run `"$streamlitAppPath`" --server.port 8502 --server.headless true"

Write-Host "Both servers are now running."
Write-Host "Flask API server: http://localhost:5000"
Write-Host "Streamlit app: http://localhost:8502"
Write-Host ""
Write-Host "To use the Chrome extension:"
Write-Host "1. Open Chrome and go to chrome://extensions/"
Write-Host "2. Enable 'Developer mode' (toggle in the top-right corner)"
Write-Host "3. Click 'Load unpacked' and select the 'app' folder in this project"
Write-Host "4. The extension should now be installed and ready to use"