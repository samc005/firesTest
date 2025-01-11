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

# Set page configuration
st.set_page_config(page_title="Wildfire Prediction Model", page_icon="🔥", layout="wide")

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
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Wildfire Prediction Model")
st.sidebar.markdown("This model predicts the likelihood of wildfire occurrence based on environmental factors. Click on the map to choose a location, and the model will fetch environmental data for prediction.")

# Map setup using Folium
m = folium.Map(location=[40.0, -120.0], zoom_start=5)  # Initial map centered on a specific location

# Adding a click listener to capture coordinates
# You can also use GeoJSON or other methods to add specific points if needed
def on_click(event):
    lat, lon = event.latlng
    st.session_state.lat = lat
    st.session_state.lon = lon

m.on_click(on_click)

# Display the map in the Streamlit app
st.markdown("### Click on the map to select a location for prediction:")
map_result = st_folium(m, width=700)

# If the user clicked on the map, extract the lat/lon
if 'lat' in st.session_state and 'lon' in st.session_state:
    lat = st.session_state.lat
    lon = st.session_state.lon
    st.write(f"**Selected Location:** Latitude: {lat}, Longitude: {lon}")

    # Simulate environmental factors based on the clicked location (this should be replaced with your model)
    def extract_environmental_factors(lat, lon):
        # Here we simulate environmental factors using random values
        temperature = random.uniform(15, 45)  # Random temperature in Celsius
        humidity = random.uniform(10, 100)    # Random humidity
        wind_speed = random.uniform(0, 100)   # Random wind speed
        precipitation = random.uniform(0, 200) # Random precipitation
        return temperature, humidity, wind_speed, precipitation

    # Fetch environmental factors
    temperature, humidity, wind_speed, precipitation = extract_environmental_factors(lat, lon)

    # Show extracted environmental factors in the main content area
    st.subheader("Extracted Environmental Factors:")
    st.write(f"**Temperature:** {temperature:.2f} °C")
    st.write(f"**Humidity:** {humidity:.2f} %")
    st.write(f"**Wind Speed:** {wind_speed:.2f} km/h")
    st.write(f"**Precipitation:** {precipitation:.2f} mm")

    # Simulate prediction (replace with your actual prediction model)
    if st.button("Predict Wildfire Likelihood"):
        prediction_score = random.random()

        # Display prediction result
        st.subheader("Prediction Result")
        if prediction_score > 0.7:
            st.markdown(f"<h2 style='color: red;'>High Likelihood of Wildfire! ({prediction_score*100:.2f}%)</h2>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h2 style='color: green;'>Low Likelihood of Wildfire ({prediction_score*100:.2f}%)</h2>", unsafe_allow_html=True)

        # Visualize the prediction with a bar chart
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


