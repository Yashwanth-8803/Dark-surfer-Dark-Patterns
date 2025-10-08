# Dark Patterns Detector - Quick Start Guide

This guide will help you deploy and run the Dark Patterns Detector project.

## Step 1: Install Dependencies

Open a command prompt and navigate to the project's API directory:

```cd

```
pip install -r requirements.txt
```

## Step 2: Generate Models

Run the model generation script:

```
python generate_models.py
```

This will:
- Load the dataset from the LLM-Model directory
- Train a presence classifier to detect dark patterns
- Train a category classifier to categorize dark patterns
- Save the models to the api directory

## Step 3: Start the API Server

Run the Flask API server:

```
python app.py
```

The server will start on http://127.0.0.1:5000

## Step 4: (Optional) Set Up the Streamlit App for Flagging Sites

The "FLAG SITE" button in the extension uses a Streamlit app to report dark patterns. To set this up:

1. Get a Google API key from https://makersuite.google.com/app/apikey

2. Create a .env file in the api directory:
   ```
   # Copy the example file
   copy .env.example .env
   ```

3. Edit the .env file and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

4. Start the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```
   
   Or use the provided batch file:
   ``` run_stream lit.bat
   ```

The Streamlit app will start on http://localhost:8501

## Step 5: Load the Chrome Extension

1. Open Google Chrome
2. Go to chrome://extensions/
3. Enable "Developer mode" (toggle in top-right)
4. Click "Load unpacked"
5. Select the "Dark-Patterns/app" folder

## Step 6: Use the Extension

1. Visit any website
2. Click the Dark Patterns Detector icon in your browser toolbar
3. Click the "ANALYZE SITE" button to detect dark patterns on the current page
4. The extension will highlight any detected dark patterns on the page
5. Click the "FLAG SITE" button to report a dark pattern using the Streamlit app

## Troubleshooting

If you encounter any issues:

1. Make sure the API server is running
2. Check the browser console for error messages
3. Verify that the model files were generated correctly in the api directory
4. If you see a "Dark Pattern" not in index error, make sure the dataset.csv file has the correct column names

## Common Issues and Solutions

### KeyError: "['Dark Pattern'] not in index"

This means the column name in the script doesn't match what's in the dataset. The generate_models.py script has been updated to use the correct column names.

### API Connection Issues

If the extension can't connect to the API:
- Make sure the API server is running
- Check that the endpoint URL in content.js is correct (http://127.0.0.1:5000/)
- Verify that no firewall is blocking the connection

### No Dark Patterns Detected

If the extension doesn't detect any dark patterns:
- Make sure the models were generated correctly
- Check the browser console for any error messages
- Try visiting a website known to have dark patterns