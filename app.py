'''import streamlit as st 
from joblib import load

#model = load("model.joblib")

st.markdown("<h1 style='text-align: center; color: #FF5733;'>Wildfire Prediction Model</h1>", unsafe_allow_html=True)



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
st.write("Results: ", prediction)
'''

import streamlit as st
import folium
from streamlit_folium import st_folium
import random

st.markdown("<h1 style='text-align: center; color: #FF5733; font-size: 50px;'>Wildfire Prediction Model</h1>", unsafe_allow_html=True)


# Add custom styles
st.markdown("""
    <style>
    /* Custom theme */
    .css-1d391kg {background-color: black; color: white;}  /* General page background color */
    .css-1s3gz7n {background-color: #FF5733; color: white;}  /* Sidebar background */
    
    /* Title styling */
    h1 {
        text-align: center;
        color: #FF5733;
    }
    
    .map-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 30px;
        margin-left: 30px;
        margin-right: 30px;
        padding-top: 0rem;
        padding-bottom: 0rem;
    }
    </style>
""", unsafe_allow_html=True)

# Add a Marker on Click (or any other interactive layer like GeoJSON)
st.markdown("<h2 style='text-align: center; color:white;'>Click on the map to select a location:</h2>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #FF5733;'>This model predicts the likelihood of wildfire occurrence based on environmental factors. Click on the map to choose a location, and the model will fetch environmental data for prediction.</p>", unsafe_allow_html=True)

st.markdown('<div class="map-container">', unsafe_allow_html=True)

# Initialize map
m = folium.Map(location=[40.0, -120.0], zoom_start=5)

folium.Marker(location=[40.0, -120.0]).add_to(m) 
m.add_child(folium.ClickForMarker()) # Add click functionality to the map

# Render the map with `st_folium`
map_result = st_folium(m, width=700)

st.markdown('</div>', unsafe_allow_html=True)

# Capture the new clicked location
if map_result and "last_clicked" in map_result:
    clicked_location = map_result["last_clicked"]
    st.session_state["clicked_location"] = clicked_location  # Update session state
    st.experimental_rerun()  # Refresh the app to update the map with the new marker


# Footer with additional information
st.markdown("""
    <div style="text-align: center; font-size: 14px; color: gray;">
        <p>Data sources: National Weather Service, Fire Prediction Model</p>
    </div>
""", unsafe_allow_html=True)

