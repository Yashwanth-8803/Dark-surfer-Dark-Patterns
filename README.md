# DarkPatternLLM

DarkPatternLLM is a project aimed at detecting and combating dark patterns on websites using advanced Language Models (LLMs). This tool provides users with a more transparent and user-friendly online experience.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Deployment](#deployment)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

### 1. Pattern Detection
The project leverages machine learning models to detect and highlight potential dark patterns on websites.

### 2. Dataset
A comprehensive dataset has been gathered from various sources to train and fine-tune the models for accurate pattern detection.

### 3. User Alerts
Receive real-time alerts when visiting a website that employs deceptive design practices.

### 4. Educational Resources
Access resources within the extension to learn more about dark patterns and how to protect yourself online.

## Installation

### Prerequisites
- Python 3.8 or higher
- Google Chrome browser

### Setup
1. Clone this repository to your local machine
2. Navigate to the project directory
3. Run the deployment script:
   ```
   python deploy.py
   ```
   This will:
   - Install all required dependencies
   - Generate the machine learning models
   - Start the API server
   - Provide instructions for loading the Chrome extension

## Deployment

The project consists of two main components:

1. **API Server**: A Flask-based backend that processes text and identifies dark patterns
2. **Chrome Extension**: A browser extension that sends webpage content to the API and highlights dark patterns

To deploy the project:

1. Run the deployment script:
   ```
   python deploy.py
   ```

2. Load the Chrome extension:
   - Open Chrome and go to `chrome://extensions/`
   - Enable "Developer mode" (toggle in the top-right corner)
   - Click "Load unpacked" and select the `app` folder in this project
   - The extension should now be installed and ready to use

## Usage

After installation, the DarkPatternLLM icon will appear in your browser toolbar. Simply visit any website, and click the "ANALYZE SITE" button in the extension popup. The extension will automatically analyze the page for dark patterns. If a dark pattern is detected, the relevant elements will be highlighted on the page with an explanation of the pattern type.

## Project Structure

- `api/`: Contains the Flask API server
  - `app.py`: Main API server code
  - `generate_models.py`: Script to generate ML models
  - `requirements.txt`: Python dependencies

- `app/`: Chrome extension files
  - `js/`: JavaScript files for the extension
  - `css/`: Styling for the extension
  - `popup.html`: Extension popup interface

- `LLM-Model/`: Model training code and datasets
  - `dataset.csv`: Training data for the models
  - Various Python scripts for model training and evaluation

## Contributing

We welcome contributions! If you want to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

---



