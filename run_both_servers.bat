@echo off
echo Starting both servers...

echo Starting Flask API Server with CORS enabled...
start cmd /k "cd api && python app.py"

echo Waiting for Flask API to initialize...
timeout /t 5 /nobreak

echo Starting Streamlit App...
start cmd /k "python run_streamlit_fixed.py"

echo Both servers are now running.
echo Flask API server: http://localhost:5000
echo Streamlit app: http://localhost:8502
echo.
echo To use the Chrome extension:
echo 1. Open Chrome and go to chrome://extensions/
echo 2. Enable 'Developer mode' (toggle in the top-right corner)
echo 3. Click 'Load unpacked' and select the 'app' folder in this project
echo 4. The extension should now be installed and ready to use
pause