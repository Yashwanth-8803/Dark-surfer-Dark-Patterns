import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from joblib import dump
import os
import sys

# Add the LLM-Model directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'LLM-Model'))

# Check if dataset.csv exists
dataset_path = os.path.join(os.path.dirname(__file__), '..', 'LLM-Model', 'dataset.csv')
if not os.path.exists(dataset_path):
    print(f"Error: Dataset file not found at {dataset_path}")
    sys.exit(1)

print("Loading dataset...")
df = pd.read_csv(dataset_path)
df = df[pd.notnull(df["text"])]

# Print column names to debug
print("Dataset columns:", df.columns.tolist())
print("First few rows:")
print(df.head())

# Generate presence classifier (Dark vs Not Dark)
print("Generating presence classifier...")
# The dataset uses 'label' column for dark pattern presence (1 = Dark, 0 = Not Dark)
df['is_dark'] = df['label'].apply(lambda x: 'Dark' if x == 1 else 'Not Dark')
presence_col = ["text", "is_dark"]
presence_df = df[presence_col]
presence_df["category_id"] = presence_df["is_dark"].factorize()[0]

X_train, X_test, y_train, y_test = train_test_split(
    presence_df['text'], presence_df['category_id'], test_size=0.3, random_state=42
)

presence_vect = CountVectorizer()
X_train_counts = presence_vect.fit_transform(X_train)

presence_clf = MultinomialNB()
presence_clf.fit(X_train_counts, y_train)

# Map numeric labels back to text labels
presence_category_id_df = presence_df[['is_dark', 'category_id']].drop_duplicates()
presence_id_to_category = dict(zip(presence_category_id_df['category_id'], presence_category_id_df['is_dark']))

# Generate category classifier
print("Generating category classifier...")
# Only use rows where label is 1 (Dark Pattern) for category classification
dark_patterns_df = df[df['label'] == 1]
print(f"Number of dark patterns for category classification: {len(dark_patterns_df)}")

if len(dark_patterns_df) == 0:
    print("Error: No dark patterns found in the dataset for category classification")
    # Create a dummy category classifier
    category_vect = CountVectorizer()
    category_vect.fit(["dummy text"])
    category_clf = MultinomialNB()
    category_id_to_category = {0: "Unknown"}
else:
    category_col = ["text", "Pattern Category"]
    category_df = dark_patterns_df[category_col]
    category_df["category_id"] = category_df["Pattern Category"].factorize()[0]

    X_train, X_test, y_train, y_test = train_test_split(
        category_df['text'], category_df['category_id'], test_size=0.3, random_state=42
    )

    category_vect = CountVectorizer()
    X_train_counts = category_vect.fit_transform(X_train)

    category_clf = MultinomialNB()
    category_clf.fit(X_train_counts, y_train)

    # Map numeric labels back to text labels
    category_id_df = category_df[['Pattern Category', 'category_id']].drop_duplicates()
    category_id_to_category = dict(zip(category_id_df['category_id'], category_id_df['Pattern Category']))

# Save models and vectorizers
print("Saving models...")
dump(presence_clf, 'presence_classifier.joblib')
dump(presence_vect, 'presence_vectorizer.joblib')
dump(presence_id_to_category, 'presence_id_to_category.joblib')

dump(category_clf, 'category_classifier.joblib')
dump(category_vect, 'category_vectorizer.joblib')
dump(category_id_to_category, 'category_id_to_category.joblib')

# Print summary
print("\nModel Generation Summary:")
print(f"Presence classifier: {len(presence_df)} samples")
print(f"Presence categories: {list(presence_id_to_category.values())}")
print(f"Category classifier: {len(dark_patterns_df) if 'dark_patterns_df' in locals() else 0} samples")
print(f"Pattern categories: {list(category_id_to_category.values())}")

print("\nModels generated successfully!")