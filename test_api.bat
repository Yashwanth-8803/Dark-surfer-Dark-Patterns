@echo off
echo Starting API Test...

echo Starting Flask API Server with CORS enabled...
start cmd /k "cd api && python app.py"

echo Waiting for Flask API to initialize...
timeout /t 5 /nobreak

echo Opening test page in browser...
start "" "api/test_api.html"

echo Test started. Check the browser window that opened.
pause