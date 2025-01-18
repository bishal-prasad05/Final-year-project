import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Heart Disease Prediction",
                   layout="wide", page_icon="❤️")

working_dir = os.path.dirname(os.path.abspath(__file__))

heart_disease_model = pickle.load(
    open(f'{working_dir}/saved_models/heart.pkl', 'rb'))

with st.sidebar:
    selected = option_menu("Coronary Artery Disease Prediction",
                           ['Data Form'
                            ],
                           menu_icon='hospital-fill',
                           icons=['heart'],
                           default_index=0)


if selected == 'Data Form':
    st.title("Coronary Artery Disease Prediction Using Machine Learning")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex (M=1 / F=0)")
    with col3:
        cp = st.text_input("Chest Pain Types (CP)")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure (RestBP)")
    with col2:
        chol = st.text_input("Serum Cholestroal in mg/dl")
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (FBS) ')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (RestECG)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved (Thalach)')

    with col3:
        exang = st.text_input('Exercise Induced Angina (Exang)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise (Oldpeak)')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (CA)')

    with col1:
        thal = st.text_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    with col1:
        separated_values=st.text_input("Enter the separated values ")
    heart_disease_result = ""
    separated_values=separated_values.split(" ")
    if st.button("Heart Disease Test Result"):
        if(separated_values!=[]):
          user_input=separated_values
        else:
          user_input = [age, sex, cp, trestbps, chol, fbs,restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        prediction = heart_disease_model.predict([user_input])
        if prediction[0] == 1:
            heart_disease_result = "This person is at high risk of heart failure or heart attack"
            print(prediction)
        else:
            heart_disease_result = "This person currently has no risk of heart attack or heart failure"
            print(prediction)
    st.success(heart_disease_result)
