import streamlit as st
import pickle
import numpy as np

# Load the trained model from the pickle file
model_filename = "stress_prediction_model_10.pkl"
with open(model_filename, 'rb') as file:
    model = pickle.load(file)


# Function to predict stress level based on user inputs
def predict_stress(inputs):
    inputs = np.array(inputs).reshape(1, -1)
    prediction = model.predict(inputs)[0]

    if prediction == 0:
        return "Low Stress"
    elif prediction == 1:
        return "Moderate Stress"
    else:
        return "High Stress"


# Streamlit application UI
st.title("Student Stress Prediction Application")

# Create a form for user inputs
with st.form(key='stress_form'):
    rainy_day_stress = st.radio("How do rainy days affect your stress?",
                                ["Relaxed", "A little stressed", "Very stressed"])
    rainy_day_stress_value = [0, 1, 2][["Relaxed", "A little stressed", "Very stressed"].index(rainy_day_stress)]

    weather_mood_stress = st.radio("How does the current weather affect your stress?",
                                   ["No effect", "Mildly affects", "Significantly affects"])
    weather_mood_stress_value = [0, 1, 2][
        ["No effect", "Mildly affects", "Significantly affects"].index(weather_mood_stress)]

    hot_weather_sleep_stress = st.radio("How does hot weather affect your sleep and stress the next day?",
                                        ["I sleep well", "Somewhat disrupted sleep", "Poor sleep and stressed"])
    hot_weather_sleep_stress_value = [0, 1, 2][
        ["I sleep well", "Somewhat disrupted sleep", "Poor sleep and stressed"].index(hot_weather_sleep_stress)]

    cold_day_productivity_stress = st.radio("How productive and stress-free are you on cold days?",
                                            ["Productive", "Less productive", "Unproductive and stressed"])
    cold_day_productivity_stress_value = [0, 1, 2][
        ["Productive", "Less productive", "Unproductive and stressed"].index(cold_day_productivity_stress)]

    cloudy_day_anxiety_stress = st.radio("How does cloudy weather affect your anxiety?",
                                         ["No anxiety", "Mild anxiety", "High anxiety"])
    cloudy_day_anxiety_stress_value = [0, 1, 2][
        ["No anxiety", "Mild anxiety", "High anxiety"].index(cloudy_day_anxiety_stress)]

    blood_pressure = st.radio("How concerned are you about your blood pressure?",
                              ["Not concerned", "Slightly concerned", "Highly concerned"])
    blood_pressure_value = [0, 1, 2][["Not concerned", "Slightly concerned", "Highly concerned"].index(blood_pressure)]

    social_support = st.radio("How much support do you feel from your social network?",
                              ["Well-supported", "Some support", "No support"])
    social_support_value = [0, 1, 2][["Well-supported", "Some support", "No support"].index(social_support)]

    mental_health_history = st.radio("Do you have a history of mental health challenges?",
                                     ["No", "Yes"])
    mental_health_history_value = [0, 1][["No", "Yes"].index(mental_health_history)]

    study_load = st.radio("How does your academic study load affect your stress?",
                          ["Manageable", "Slightly overwhelmed", "Very overwhelmed"])
    study_load_value = [0, 1, 2][["Manageable", "Slightly overwhelmed", "Very overwhelmed"].index(study_load)]

    sleep_quality = st.radio("How does your sleep quality affect your stress?",
                             ["Good sleep", "Moderate sleep", "Poor sleep and stressed"])
    sleep_quality_value = [0, 1, 2][["Good sleep", "Moderate sleep", "Poor sleep and stressed"].index(sleep_quality)]

    # Submit button
    submit_button = st.form_submit_button(label='Predict Stress Level')

# Predict and display the result when form is submitted
if submit_button:
    # Gather inputs
    user_inputs = [
        rainy_day_stress_value,
        weather_mood_stress_value,
        hot_weather_sleep_stress_value,
        cold_day_productivity_stress_value,
        cloudy_day_anxiety_stress_value,
        blood_pressure_value,
        social_support_value,
        mental_health_history_value,
        study_load_value,
        sleep_quality_value
    ]

    # Predict stress level
    result = predict_stress(user_inputs)

    # Display result
    st.write(f"Predicted Stress Level: {result}")
