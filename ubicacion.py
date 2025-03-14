import streamlit as st
from streamlit_geolocation import streamlit_geolocation
from datetime import datetime
import pytz  # Add this import for timezone support

def get_location():
    """
    Function to obtain latitude and longitude using streamlit-geolocation
    
    Returns:
        dict: Contains latitude, longitude, and other location information if successful
    """
    # Initialize session state for location data if it doesn't exist
    if 'location_data' not in st.session_state:
        st.session_state.location_data = None
        
    # Initialize session state for date and time if they don't exist
    if 'current_date' not in st.session_state:
        st.session_state.current_date = None
    
    if 'current_time' not in st.session_state:
        st.session_state.current_time = None
    
    # Create a location button
    location = streamlit_geolocation()
    
    # Update session state if location is obtained
    if location and location != st.session_state.location_data:
        st.session_state.location_data = location
    
        # Get the current UTC time
        utc_now = datetime.now(pytz.UTC)
        
        # Convert to Eastern Time (ET)
        eastern = pytz.timezone('US/Eastern')
        et_now = utc_now.astimezone(eastern)
        
        # Update date and time in Eastern Time
        st.session_state.current_date = et_now.strftime("%m-%d-%Y")
        st.session_state.current_time = et_now.strftime("%H:%M")
    
        st.rerun()
    
    # Display the results if location data exists
    if st.session_state.location_data:
        st.markdown("---")
        col1, col2 = st.columns(2)
    
        with col1:
            st.write("Fecha")
            st.write(st.session_state.current_date if st.session_state.current_date else "None")
    
            st.write("Latitud:", location.get("latitude"))

        with col2:
            st.write("Hora")
            st.write(st.session_state.current_time if st.session_state.current_time else "None")
            st.write("Longitud:", location.get("longitude"))

        # Return the location data
        return st.session_state.location_data
    else:
        st.info("Click the 'Get Location' button to fetch your coordinates")
        return None
    # End of get_location function

def reset_app():
    """
    Function to completely reset the application state
    """
    # Clear all session state variables
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    
    # Display a success message
    st.success("All data has been reset!")
    
    # Force a rerun to refresh the page
    st.rerun()


if __name__ == "__main__":
    st.title("Geolocalización")
    st.write("Esta App genera sus coordenadas para certificar su ubicacion.")
    
    location_data = get_location()
    
    if location_data:
        # Example: Show location on a map
        if location_data.get("latitude") and location_data.get("longitude"):
            map_data = {
                "latitude": [location_data.get("latitude")],
                "longitude": [location_data.get("longitude")]
            }
            st.map(map_data)
    # Add a separator before the reset button
    st.markdown("---")

    # Reset button placed at the bottom of the app with enhanced styling
    if st.button("Borrar Datos", type="primary", use_container_width=False): reset_app()