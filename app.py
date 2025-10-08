from flask import Flask, jsonify, request
from flask_cors import CORS
from joblib import load
from dark_pattern_types import DarkPatternType

# Load models and vectorizers
try:
    presence_classifier = load('presence_classifier.joblib')
    presence_vect = load('presence_vectorizer.joblib')
    presence_id_to_category = load('presence_id_to_category.joblib')
    category_classifier = load('category_classifier.joblib')
    category_vect = load('category_vectorizer.joblib')
    category_id_to_category = load('category_id_to_category.joblib')
except FileNotFoundError:
    print("Model files not found. Please run generate_models.py first.")

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # ✅ Enables CORS for all routes and origins

@app.route('/', methods=['GET'])
def home():
    return '''
    <h2>Dark Pattern Analyzer API is running!</h2>
    <p>Send a <strong>POST</strong> request with JSON payload to analyze tokens.</p>
    <p>Example JSON body:</p>
    <pre>{
  "tokens": ["subscribe now", "free trial", "limited offer"]
}</pre>
    '''

@app.route('/', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'tokens' not in data:
        return jsonify({'error': 'No tokens provided. Please send JSON with "tokens" key.'}), 400

    tokens = data.get('tokens', [])
    output = []

    for token in tokens:
        try:
            # Predict if the token is a dark pattern
            presence_numeric = presence_classifier.predict(presence_vect.transform([token]))[0]
            presence_result = presence_id_to_category.get(presence_numeric, "Not Dark")

            if presence_result == 'Dark':
                try:
                    # Predict the category of the dark pattern
                    category_numeric = category_classifier.predict(category_vect.transform([token]))[0]
                    category_result = category_id_to_category.get(category_numeric, "Unknown")

                    if category_result.lower() in [dp.value for dp in DarkPatternType]:
                        print(f"Detected new dark pattern type: {category_result}")

                    output.append(category_result)
                except Exception as e:
                    print(f"Error predicting category: {e}")
                    output.append("Unknown")
            else:
                output.append(presence_result)
        except Exception as e:
            print(f"Error processing token: {e}")
            output.append("Not Dark")  # Default to not dark on error

    # Debug print
    dark_tokens = [tokens[i] for i in range(len(output)) if output[i] != 'Not Dark']
    if dark_tokens:
        print("\nDetected Dark Patterns:")
        for i, d in enumerate(dark_tokens):
            print(f"{i+1}. {d}")
    print("\nTotal 'Dark' tokens:", len(dark_tokens))

    return jsonify({'result': output})

if __name__ == '__main__':
    # 0.0.0.0 allows access from Chrome extensions and other devices
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
