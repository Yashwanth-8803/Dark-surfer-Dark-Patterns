# Dark Patterns Detector - Deployment Instructions

## Prerequisites
- Python 3.8 or higher
- Google Chrome browser

## Deployment Steps

### 1. Install Python Dependencies
Open a command prompt in the Dark-Patterns/api directory and run:
```
pip install -r requirements.txt
```

### 2. Generate Machine Learning Models
Navigate to the Dark-Patterns/api directory and run:
```
python generate_models.py
```
This will create the necessary model files in the api directory.

### 3. Start the API Server
In the Dark-Patterns/api directory, run:
```
python app.py
```
This will start the Flask server on http://127.0.0.1:5000.

### 4. Load the Chrome Extension
1. Open Google Chrome
2. Navigate to chrome://extensions/
3. Enable "Developer mode" (toggle in the top-right corner)
4. Click "Load unpacked" and select the Dark-Patterns/app folder
5. The extension should now appear in your browser toolbar

## Using the Extension
1. Visit any website
2. Click on the Dark Patterns Detector extension icon
3. Click the "ANALYZE SITE" button
4. The extension will scan the page and highlight any detected dark patterns

## Troubleshooting
- If the extension doesn't detect any patterns, make sure the API server is running
- Check the browser console for any error messages
- Ensure all model files are generated correctly in the api directory