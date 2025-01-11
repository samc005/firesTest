import streamlit as st 
from joblib import load

#model = load("model.joblib")

st.set_page_config(layout="wide", page_title="Wildfire Prediction Model", page_icon=":fire:")


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
