import streamlit as st
import folium
from streamlit_folium import st_folium
import numpy as np
import pandas as pd
from joblib import load
import math
import datetime

from getData import get_weather_data

model = load('model.joblib')

# Function to prepare data for the model
def prepare_data(input_data):
   data = input_data.split()
   user_df = pd.DataFrame([data], columns=[
      'month', 'temp', 'RH', 'wind', 'rain',
   ])
   user_df['month'] = pd.to_numeric(user_df['month'])
   user_df['temp'] = pd.to_numeric(user_df['temp'])
   user_df['RH'] = pd.to_numeric(user_df['RH'])
   user_df['wind'] = pd.to_numeric(user_df['wind'])
   user_df['rain'] = pd.to_numeric(user_df['rain'])

   return user_df

# Function to make predictions (modify according to your model's input requirements)
def predict(processed_data):
   # Preprocess input data if necessary (e.g., scaling, reshaping, etc.)
   #  input_data = np.array(input_data).reshape(1, -1)  # Example
   prediction = model.predict(processed_data)
   return prediction

def is_within_radius(predicted_radius, point, center=(0, 0)):
   """
   Determines if a given point is within the circle defined by a predicted radius 
   with a ±20% margin of error.

   :param predicted_radius: The predicted radius of the circle.
   :param point: A tuple (x, y) representing the coordinates of the point.
   :param center: The center of the circle (default is (0, 0)).

   :return: A message indicating whether the point is inside the circle or not.
   """
   # Calculate the Euclidean distance from the center to the point
   distance = math.sqrt((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2)

   # Calculate the actual radius range (80% to 120% of predicted radius)
   min_radius = predicted_radius * 0.8
   max_radius = predicted_radius * 1.2

   # Check if the point is within the circle's range
   if min_radius <= distance <= max_radius:
      return f"<p style='text-align: center;'>You are within the high-risk radius of {predicted_radius[0]} (±20% error).</p>"
   else:
      return f"<p style='text-align: center;'>You are safe outside the high-risk radius of {predicted_radius[0]} (±20% error).</p>"

def print_result(prediction):
   point = (latitude, longitude)  # Example point coordinates
   result = is_within_radius(prediction, point)
   return result


#styles
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@800&display=swap' rel="stylesheet")

    /* Custom theme */
    .css-1d391kg {background-color: black; color: white;}  /* General page background color */
    
    /* Title styling */
    h1 {
        font-family: 'Raleway', serif;
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
        transition: 0.3s ease; 
    }
    .content {
        margin-top: 60px; /* Add margin to push content below the navbar */
    }
    </style>
""", unsafe_allow_html=True)

#tabs (links)
st.markdown("""
    <div class="navbar">
        <a href="?page=Home" class="{% if page == 'Home' %}active{% endif %}">Home</a>
        <a href="?page=resources" class="{% if page == 'resources' %}active{% endif %}">Resources</a>
        <a href="?page=chatbot" class="{% if page == 'chatbot' %}active{% endif %}">Chatbot</a>
    </div>
""", unsafe_allow_html=True)

# Get query params from URL
query_params = st.experimental_get_query_params()

#current page from URL query param
tab = query_params.get("page", ["Home"])[0]  # Default to "home" if no parameter

if tab == "Home":
    # Click
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 50px;'>WILDFIRE PREDICTION MODEL</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white; font-size: 25px;'>Click on the map to select a location:</h2>", unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; color: #FF5733;'>This model predicts the likelihood of wildfire occurrence based on environmental factors. Click on the map to choose a location, and the model will fetch environmental data for prediction.</p>", unsafe_allow_html=True)

    st.markdown('<div class="map-container">', unsafe_allow_html=True)

    # Initialize map
    m = folium.Map(location=[40.0, -120.0], zoom_start=5)

    fire_icon = folium.Icon(icon="cloud", icon_color="orange", color="red")

    click_marker = folium.ClickForMarker(popup="Fire Marker", icon=fire_icon)

    click_marker.add_to(m)

    # Render map 
    map_result = st_folium(m, width=700)

    st.markdown('</div>', unsafe_allow_html=True)

    if map_result and "last_clicked" in map_result: 
        clicked_location = map_result["last_clicked"]

        if clicked_location and "lat" in clicked_location and "lng" in clicked_location:
            latitude = clicked_location["lat"]
            longitude = clicked_location["lng"]
                        
            weather_data = get_weather_data(latitude, longitude)

            if weather_data:
                current_date = datetime.datetime.now()
                user_input = str(current_date.month-1) + " "
                user_input += str(weather_data['temperature']) + " "
                user_input += str(weather_data['humidity']) + " "
                user_input += str(weather_data['wind_speed']) + " "
                user_input += str(weather_data['precipitation'])
                input_data = prepare_data(user_input)
                prediction = predict(input_data)
                st.markdown(f"<p style='text-align: center;'>{print_result(prediction)}</p>", unsafe_allow_html=True)

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
        else:
            st.markdown("<p style='text-align: center;'>Please click on the map.</p>", unsafe_allow_html=True)


    # Footer
    st.markdown("""
        <div style="text-align: center; font-size: 14px; color: gray;">
            <p>Data sources: National Weather Service, Fire Prediction Model</p>
        </div>
    """, unsafe_allow_html=True)

elif tab == "resources":
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Raleway; font-size: 50px;'>SAFETY TIPS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; '>Here, we provide information and resources related to wildfire safety and prevention.</p>", unsafe_allow_html=True)
    st.image("https://cdn.kqed.org/wp-content/uploads/sites/10/2025/01/GettyImages-2193000280-1020x653.jpg", caption="Crowd watching Palisades Fire from Santa Monica, California on January 8, 2025. (Tiffany Rose/Getty Images)", use_column_width=True)
   
    st.markdown("<p style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 20px;'>Some tips: </p>", unsafe_allow_html=True)
    st.markdown("<p style ='text-align: center; color: white; font-family: Georgia; font-size: 15px;'>Have emergency supplies prepared. Pack essentials like water, food, and medicine.</p>", unsafe_allow_html=True)
    st.markdown("<p style ='text-align: center; color: white; font-family: Georgia; font-size: 15px;'>Monitor fires and the weather around you regularly.</p>", unsafe_allow_html=True)
    st.markdown("<p style ='text-align: center; color: white; font-family: Georgia; font-size: 15px;'>Learn emergency skills such as CPR and First Aid.</p>", unsafe_allow_html=True)
    st.markdown("<p style ='text-align: center; color: white; font-family: Georgia; font-size: 15px;'>Plan to not have access to electricity or the internet.
</p>", unsafe_allow_html=True)
    st.markdown("<p style ='text-align: center; color: white; font-family: Georgia; font-size: 15px;'>Keep personal records safe.</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 20px;'>Contact the Federal Emergency Management Agency (FEMA):</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-family: Georgia; font-size: 15px;'>https://www.disasterassistance.gov/</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 20px;'>Create your own wildfire action plan:</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-family: Georgia; font-size: 15px;'>https://readyforwildfire.org/prepare-for-wildfire/wildfire-action-plan/</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 20px;'>General information about wildfires:</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-family: Georgia; font-size: 15px;'>https://namica.org/wildfires/</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 20px;'>Helpline for counseling (related to natural/man-made disasters):", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-family: Georgia; font-size: 15px;'>https://www.samhsa.gov/find-help/helplines/disaster-distress-helpline</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 20px;'>Resources to recover from wildfires:</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-family: Georgia; font-size: 15px;'>https://www.cdfa.ca.gov/firerecovery/</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 20px;'>External list of organizations/programs that can help with wildfire recovery:</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-family: Georgia; font-size: 15px;'>https://readyforwildfire.org/post-wildfire/who-can-help</p>", unsafe_allow_html=True)
    
elif tab == "chatbot":
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Raleway; font-size: 50px;'>TALK TO US</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; '>Ask any questions about wildfires and get predictions and safety tips!</p>", unsafe_allow_html=True)
    user_input = st.text_input("Ask a question:")
    if user_input:
        st.write(f"You asked: {user_input}")
        st.write("Chatbot response: [Simulated Answer] Stay safe and prepared for wildfires!")
