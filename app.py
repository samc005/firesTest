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

#styles
st.markdown("""
    <style>
    /* Custom theme */
    .css-1d391kg {background-color: black; color: white;}  /* General page background color */
    
    /* Title styling */
    h1 {
        text-align: center;
        color: #FF5733;
    }
    
    .map-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 5px;
        margin-left: 30px;
        margin-right: 30px;
        padding-top: 0rem;
        padding-bottom: 0rem;
    }
    </style>
""", unsafe_allow_html=True)

#navigation bar
st.markdown("""
    <style>
    .css-18e3th9 { 
        padding-top: 0rem; 	
        padding-bottom: 0rem; 
    }

    body {
        margin: 0;
        padding: 0;
    }
    .navbar {
        background-color: #FF5733;
        padding: 5px 0;
        text-align: center;
        top: 0;
        width: 100%;
        z-index: 1000;
    }

    .navbar a {
        color: white;
        padding: 7px 10px;
        text-decoration: none;
        font-size: 18px;
        display: inline-block;
    }

    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    .content {
        margin-top: 60px; /* Add margin to push content below the navbar */
    }
    </style>
""", unsafe_allow_html=True)

#tabs (links)
st.markdown("""
    <div class="navbar">
        <a href="">Home</a>
        <a href="?page=resources">Resources</a>
        <a href="?page=chatbot">Chatbot</a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 50px;'>WILDFIRE PREDICTION MODEL</h1>", unsafe_allow_html=True)

# Get query params from URL
query_params = st.experimental_get_query_params()

#current page from URL query param
tab = query_params.get("page", ["Home"])[0]  # Default to "home" if no parameter

if tab == "Home":
    # Click
    st.markdown("<h2 style='text-align: center; font-family: Georgia; color: white;'>Click on the map to select a location:</h2>", unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; color: #FF5733;'>This model predicts the likelihood of wildfire occurrence based on environmental factors. Click on the map to choose a location, and the model will fetch environmental data for prediction.</p>", unsafe_allow_html=True)

    st.markdown('<div class="map-container">', unsafe_allow_html=True)

    # Initialize map
    m = folium.Map(location=[40.0, -120.0], zoom_start=5)

    folium.Marker(location=[40.0, -120.0]).add_to(m) 
    m.add_child(folium.ClickForMarker()) # Add click functionality to the map

    # Render map 
    map_result = st_folium(m, width=700)

    st.markdown('</div>', unsafe_allow_html=True)

    
    if "" in "last_clicked":
        st.write("Please choose a location")
    elif map_result and "last_clicked" in map_result: 
            clicked_location = map_result["last_clicked"]
            latitude = clicked_location["lat"]
            longitude = clicked_location["lng"]

    
    # Display latitude and longitude separately
    st.markdown(
        f"""
        <p style='text-align: center;'>
            <strong>Latitude:</strong> {latitude:.6f} <br>
            <strong>Longitude:</strong> {longitude:.6f}
        </p>
        """,
        unsafe_allow_html=True,
    )

    # Footer
    st.markdown("""
        <div style="text-align: center; font-size: 14px; color: gray;">
            <p>Data sources: National Weather Service, Fire Prediction Model</p>
        </div>
    """, unsafe_allow_html=True)

elif tab == "resources":
    st.title("Resources")
    st.write("Here, we provide resources related to wildfire prevention and safety.")
    st.markdown("[Link to more resources](https://www.nasa.gov/feature/nasa-develops-wildfire-prediction-model)")

elif tab == "chatbot":
    st.title("Chat with Our Wildfire Chatbot")
    st.write("Ask any questions about wildfires and get predictions and safety tips!")
    user_input = st.text_input("Ask a question:")
    if user_input:
        st.write(f"You asked: {user_input}")
        st.write("Chatbot response: [Simulated Answer] Stay safe and prepared for wildfires!")


