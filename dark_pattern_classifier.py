import requests
import json
import re

class DarkPatternClassifier:
    def __init__(self):
        self.system_prompt = """
You are an expert in identifying dark patterns on websites. Dark patterns are user interface design choices 
that benefit an online service by leading users into making decisions they might not otherwise make.

Analyze the provided text and determine:
1. If it contains dark patterns
2. What type of dark pattern it is (Urgency, Scarcity, Social Proof, Misdirection, Obstruction, Sneaking, Forced Action)
3. How it might manipulate users

Respond only with a JSON object in the following format:
{
  "is_dark_pattern": true,
  "pattern_type": "Type of pattern or null if not a dark pattern",
  "explanation": "Brief explanation of why this is or isn't a dark pattern"
}
Do not include any other text outside the JSON block.
"""
        self.model_url = "http://localhost:11434/api/generate"
        self.model_name = "llama3"  # Use "mistral" if LLaMA3 is verbose or inconsistent

    def extract_json_block(self, text):
        """
        Attempt to extract and parse a JSON object from the model output.
        Matches the first valid-looking JSON block using regex.
        """
        match = re.search(r"\{\s*\"is_dark_pattern\".*?\}", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                return None
        return None

    def classify(self, text):
        """
        Sends the prompt to the local model and attempts to classify the text.
        Tries parsing direct JSON first, and falls back to extracting embedded JSON if needed.
        """
        full_prompt = f"{self.system_prompt}\n\nText to analyze: {text}"
        try:
            response = requests.post(
                self.model_url,
                json={"model": self.model_name, "prompt": full_prompt, "stream": False}
            )
            response.raise_for_status()  # Raises error for non-2xx responses

            result = response.json()
            raw_output = result.get("response", "").strip()

            # Attempt to directly parse JSON output
            try:
                return json.loads(raw_output)
            except json.JSONDecodeError:
                # Fallback: try to extract JSON block from a noisy response
                extracted = self.extract_json_block(raw_output)
                if extracted:
                    return extracted

                return {
                    "is_dark_pattern": None,
                    "pattern_type": None,
                    "explanation": f"Model response could not be parsed as JSON: {raw_output}"
                }

        except requests.RequestException as e:
            return {
                "is_dark_pattern": None,
                "pattern_type": None,
                "explanation": f"HTTP request failed: {str(e)}"
            }
        except Exception as e:
            return {
                "is_dark_pattern": None,
                "pattern_type": None,
                "explanation": f"Unexpected error: {str(e)}"
            }
