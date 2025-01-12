import streamlit as st
import folium
from streamlit_folium import st_folium
import random

from getData import get_weather_data

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

# Get query params from URL
query_params = st.experimental_get_query_params()

#current page from URL query param
tab = query_params.get("page", ["Home"])[0]  # Default to "home" if no parameter

if tab == "Home":
    # Click
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 50px;'>WILDFIRE PREDICTION MODEL</h1>", unsafe_allow_html=True)
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

    if map_result and "last_clicked" in map_result: 
        clicked_location = map_result["last_clicked"]

        if clicked_location and "lat" in clicked_location and "lng" in clicked_location:
            latitude = clicked_location["lat"]
            longitude = clicked_location["lng"]
                        
            weather_data = get_weather_data(latitude, longitude)

            if weather_data:
                st.write("Weather Data for Location:")
                for key, value in weather_data.items():
                    st.write(f"{key}: {value}")

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
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 50px;'>WHERE TO FIND HELP</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; '>Here, we provide resources related to wildfire prevention and safety.</p>", unsafe_allow_html=True)
    st.image("https://cdn.kqed.org/wp-content/uploads/sites/10/2025/01/GettyImages-2193000280-1020x653.jpg", caption="Crowd watching Palisades Fire from Santa Monica, California on January 8, 2025. (Tiffany Rose/Getty Images)", use_column_width=True)
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
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Georgia; font-size: 50px;'>TALK TO US</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; '>Ask any questions about wildfires and get predictions and safety tips!</p>", unsafe_allow_html=True)
    user_input = st.text_input("Ask a question:")
    if user_input:
        st.write(f"You asked: {user_input}")
        st.write("Chatbot response: [Simulated Answer] Stay safe and prepared for wildfires!")


