'''if map_result:
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
'''