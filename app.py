import streamlit as st 
from joblib import load

#model = load("model.joblib")

[theme]
primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#31333F"
font="sans serif"

st.title("Wildfire Prediction Model")


def get_input():
    elevation = st.number_input("Elevation (m): ")
    population = st.number_input("Population: ")
    input_features = [[elevation, population]]
    return input_features

def predict(model, input):
    return model.predict(input)

#def get_prediction():


input_features = get_input()
#prediction = predict(model, input_features)
#get_prediction(prediction)
st.write("Results")
