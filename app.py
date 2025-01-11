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
    
    /* Custom input box styling */
    .stTextInput>div>input {
        border: 2px solid #FF5733;
        border-radius: 5px;
        background-color: black;
        color: white;
    }
    
    /* Styling for the buttons */
    .css-1g4w6y2 {
        background-color: #FF5733;
        color: white;
        font-size: 18px;
    }
    .map-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 500px;  
        margin-top: 30px;
        margin-left: 30px;
        margin-right: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize map
m = folium.Map(location=[40.0, -120.0], zoom_start=5)

# Add a Marker on Click (or any other interactive layer like GeoJSON)
st.markdown("<h1 style='text-align: center; color:white;'>Click on the map to select a location:</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #FF5733;'>This model predicts the likelihood of wildfire occurrence based on environmental factors. Click on the map to choose a location, and the model will fetch environmental data for prediction.</p>", unsafe_allow_html=True)

st.markdown('<div class="map-container">', unsafe_allow_html=True)

# Render the map with `st_folium`
map_result = st_folium(m, width=700)

# Capture the clicked coordinates from the map result
if map_result:
    # The result will contain the coordinates of the clicked location
    clicked_lat = map_result.get('lat')
    clicked_lon = map_result.get('lon')

    if clicked_lat and clicked_lon:
        st.write(f"**Selected Location:** Latitude: {clicked_lat}, Longitude: {clicked_lon}")

        # Simulate environmental data extraction
        def extract_environmental_factors(lat, lon):
            temperature = random.uniform(15, 45)  # Random temperature in Celsius
            humidity = random.uniform(10, 100)    # Random humidity
            wind_speed = random.uniform(0, 100)   # Random wind speed
            precipitation = random.uniform(0, 200) # Random precipitation
            return temperature, humidity, wind_speed, precipitation

        # Fetch environmental factors based on the clicked location
        temperature, humidity, wind_speed, precipitation = extract_environmental_factors(clicked_lat, clicked_lon)

        # Display the environmental factors
        st.subheader("Environmental Factors:")
        st.write(f"**Temperature:** {temperature:.2f} °C")
        st.write(f"**Humidity:** {humidity:.2f} %")
        st.write(f"**Wind Speed:** {wind_speed:.2f} km/h")
        st.write(f"**Precipitation:** {precipitation:.2f} mm")
        
        # Simulate prediction (replace with your actual prediction model)
        if st.button("Predict Wildfire Likelihood"):
            prediction_score = random.random()

            st.subheader("Prediction Result")
            if prediction_score > 0.7:
                st.markdown(f"<h2 style='color: red;'>High Likelihood of Wildfire! ({prediction_score*100:.2f}%)</h2>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h2 style='color: green;'>Low Likelihood of Wildfire ({prediction_score*100:.2f}%)</h2>", unsafe_allow_html=True)

            # Optionally display a chart or more visuals (using matplotlib or others)
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            ax.bar(["Prediction"], [prediction_score], color="orange")
            ax.set_ylim(0, 1)
            st.pyplot(fig)

# Footer with additional information
st.markdown("""
    <div style="text-align: center; font-size: 14px; color: gray;">
        <p>Data sources: National Weather Service, Fire Prediction Model</p>
        <p>For more information, visit <a href="https://www.nasa.gov/feature/nasa-develops-wildfire-prediction-model" target="_blank">NASA Wildfire Prediction</a></p>
    </div>
""", unsafe_allow_html=True)

