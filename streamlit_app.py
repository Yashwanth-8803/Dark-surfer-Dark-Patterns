import streamlit as st
import json
import os
import sys
import re
from dark_pattern_classifier import DarkPatternClassifier

# Helper function to extract JSON from text
def extract_json_block(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            return None
    return None

def main():
    st.set_page_config(
        page_title="Dark Pattern Classifier",
        page_icon="🔍",
        layout="wide"
    )

    st.title("Dark Pattern Classifier")
    st.markdown("""
    This app helps identify and classify dark patterns on websites. 
    Dark patterns are user interface design choices that benefit an online service by leading users into making decisions they might not otherwise make.
    """)

    try:
        # Initialize the classifier
        classifier = DarkPatternClassifier()

        # Create tabs for different functionalities
        tab1, tab2 = st.tabs(["Analyze Text", "Report Website"])

        with tab1:
            st.header("Analyze Text for Dark Patterns")

            # Text input area
            text_input = st.text_area("Enter text to analyze:", height=200)

            if st.button("Analyze", key="analyze_button"):
                if text_input:
                    with st.spinner("Analyzing..."):
                        # Get classification result
                        response = classifier.classify(text_input)

                        # Check for API quota error
                        if isinstance(response, str) and "429" in response:
                            st.error("🚫 API quota exceeded. Please try again later.")
                            st.markdown("""
                            **Error Details:**  
                            You have exceeded the number of allowed requests to the Gemini API.  
                            - If you're using a free tier, wait a few minutes or check your usage on [Google Cloud Console](https://console.cloud.google.com/iam-admin/quotas).  
                            - To resolve permanently, upgrade your quota or reduce API call frequency.
                            """)
                            st.stop()

                        # Try extracting the JSON block
                        result_dict = extract_json_block(response) if isinstance(response, str) else response

                        if result_dict is None:
                            st.warning("Could not parse JSON from model response. Raw output:")
                            st.code(response)
                        else:
                            # Display results
                            col1, col2 = st.columns(2)

                            with col1:
                                if result_dict.get("is_dark_pattern", False):
                                    st.error("⚠️ Dark Pattern Detected")
                                else:
                                    st.success("✅ No Dark Pattern Detected")

                            with col2:
                                if result_dict.get("pattern_type"):
                                    st.info(f"Pattern Type: {result_dict['pattern_type']}")

                            st.markdown("### Explanation")
                            st.write(result_dict.get("explanation", "No explanation provided"))

                            with st.expander("View Raw Result"):
                                st.json(result_dict)
                else:
                    st.warning("Please enter some text to analyze.")

        with tab2:
            st.header("Report a Website with Dark Patterns")

            # Form for reporting a website
            with st.form("report_form"):
                website_url = st.text_input("Website URL:")
                description = st.text_area("Describe the dark pattern you found:", height=150)
                pattern_type = st.selectbox(
                    "Type of Dark Pattern:",
                    [
                        "Urgency",
                        "Scarcity",
                        "Social Proof",
                        "Misdirection",
                        "Obstruction",
                        "Sneaking",
                        "Forced Action",
                        "Other"
                    ]
                )

                if pattern_type == "Other":
                    other_type = st.text_input("Specify the pattern type:")

                screenshot = st.file_uploader("Upload a screenshot (optional):", type=["png", "jpg", "jpeg"])

                submit_button = st.form_submit_button("Submit Report")

                if submit_button:
                    if website_url and description:
                        st.success("Thank you for your report! It has been submitted for review.")

                        # Display the report details
                        st.subheader("Report Details")
                        st.write(f"**Website:** {website_url}")
                        st.write(f"**Pattern Type:** {other_type if pattern_type == 'Other' else pattern_type}")
                        st.write(f"**Description:** {description}")

                        if screenshot:
                            st.image(screenshot, caption="Uploaded Screenshot", use_column_width=True)
                    else:
                        st.warning("Please fill in the required fields (Website URL and Description).")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please make sure your local model (Ollama) is running correctly and try again.")

if __name__ == "__main__":
    main()
