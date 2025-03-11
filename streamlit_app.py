import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import datetime
import json
import time
import pandas as pd


st.header("Ubicacion")
st.write("Por favor de click en el boton, tome pantallazo y compartalo para certificar la ubicacion.") 

# Display the current date and time
current_date  = datetime.datetime.now().strftime("%m-%d-%Y") 
current_time  = datetime.datetime.now().strftime("%H:%M") 

# Get the location data
# Extract latitude and longitude
loc = get_geolocation() 
latitude = loc['coords']['latitude']
longitude = loc['coords']['longitude']

# Button to fetch location details
if st.button("Ubicación y Hora"):
    
    # Display the current date and time
    st.write(f"Fecha: {current_date}")
    st.write(f"Hora: {current_time}")

    # Create a Google Maps link
    st.write(f"Latitude: {latitude}")
    st.write(f"Longitude: {longitude}")
    st.write(f"[Google Maps](https://www.google.com/maps/search/?api=1&query={latitude},{longitude})")
    # Display the latitude and longitude

data = pd.DataFrame({
    'lat': [latitude],  # Latitude values
    'lon': [longitude]  # Use negative values for west
})

st.map(data)
