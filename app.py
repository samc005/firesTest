import streamlit as st 
from joblib import load

#model = load("model.joblib")


import streamlit as st

# Center the title using HTML
st.markdown("<h1 style='text-align: center; color: rgb(227, 92, 55);'>Wildfire Prediction Model</h1>", unsafe_allow_html=True)



def get_input():
    elevation = st.number_input("Elevation (m): ")
    population = st.number_input("Population: ")
    input_features = [[elevation, population]]
    return input_features

def predict(model, input):
    return model.predict(input)

#def get_prediction():


input_features = get_input()
prediction = predict(model, input_features)
#get_prediction(prediction)
st.write("Results: ", prediction)
