import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Title of the app
st.title("Delay Type Predictor")

# Load the "top_50_features_with_category.csv" file
@st.cache_data
def load_data():
    file_path = "top50_new_rf.csv"  # Path to your updated CSV
    return pd.read_csv(file_path)

# Load the trained model
@st.cache_resource
def load_model():
    model_path = "RF.pkl"  # Path to your saved model
    return joblib.load(model_path)

# Prepare user selections into a model-compatible input vector
def prepare_input(user_selections, all_features):
    input_features = [1 if feature in user_selections.values() else 0 for feature in all_features]
    return np.array(input_features).reshape(1, -1)

# Function to clean labels
def clean_label(feature):
    prefixes = ["incident_", "line_", "timeType_", "seasonType_", "day_of_week_", "bound_", "location_"]
    for prefix in prefixes:
        if feature.startswith(prefix):
            return feature.replace(prefix, "").replace("_", " ").title()
    return feature

# Load data and model
data = load_data()
model = load_model()

# Sidebar for user inputs
st.sidebar.header("Select Features for Each Category")

# Extract unique categories and their features
categories = data['Category'].unique()  # Get unique categories
category_feature_mapping = {
    category: data[data['Category'] == category]['Feature'].tolist() for category in categories
}

# Dropdowns for each category
user_selections = {}
for category in categories:
    # Get features for this category
    original_features = category_feature_mapping[category]
    
    # Create display-friendly labels
    friendly_labels = ["Others"] + [clean_label(feature) for feature in original_features]
    
    # Create dropdown with user-friendly labels
    selected_label = st.sidebar.selectbox(
        f"{category}:",
        options=friendly_labels,
        index=0  # Default to "Others"
    )
    
    # Map back the selected label to the original feature name
    if selected_label == "Others":
        user_selections[category] = "Others"
    else:
        original_feature_index = friendly_labels.index(selected_label) - 1  # Adjust for "Others"
        user_selections[category] = original_features[original_feature_index]


# Submit button
if st.sidebar.button("Submit"):
    st.subheader("Your Selections")
    for category, feature in user_selections.items():
        if feature != "Others":  # Avoid showing "Others"
            cleaned_feature = clean_label(feature)  # Format the feature name
            st.write(f"**{category}:** {cleaned_feature}")

    # Filter out "Others"
    selected_features = [feature for feature in user_selections.values() if feature != "Others"]

    if not selected_features:
        st.warning("Please select at least one feature before submitting.")
    else:
        # Prepare input for the model
        all_features = data['Feature'].tolist()  # All top 50 features in correct order
        input_data = prepare_input(user_selections, all_features)

        # Predict the delay type and get probabilities
        prediction = model.predict(input_data)  # Most likely delay type
        probabilities = model.predict_proba(input_data)[0]  # Probabilities for each class

        # Define descriptions for each delay type
        delay_type_descriptions = {
            1: "short delay - 5 minutes or less",
            2: "normal delay - between 6 minutes and 15 minutes",
            3: "long delay - 16 minutes or more"
        }

        # Format probabilities for display with descriptions
        probability_output = [
            f"{round(prob * 100, 2)}% chance it is Delay Type {i + 1} ({delay_type_descriptions[i + 1]})"
            for i, prob in enumerate(probabilities)
        ]

        # Display the most likely delay type
        st.subheader("Predicted Delay Type")
        st.success(f"The most likely delay type is: **Delay Type {prediction[0]}**")

        # Display probabilities as a list
        st.subheader("Class Probabilities")
        for line in probability_output:
            st.write(f"- {line}")




