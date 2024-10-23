import folium
from geopy.geocoders import Nominatim
import time

# Provide a custom user agent
geolocator = Nominatim(user_agent="my-custom-application")

# Ask user for input location
location_input = input("Enter a location: ")

# Geocode the user-provided location
location = geolocator.geocode(location_input)

# If geocoding fails, retry or handle the error
if not location:
    print("Location not found")
else:
    # Create a Folium map centered on the geocoded coordinates
    m = folium.Map(location=[location.latitude, location.longitude], zoom_start=7)

    # Add a marker for the geocoded location
    folium.Marker([location.latitude, location.longitude], popup=location_input).add_to(m)

    # Save map to HTML file
    m.save('map.html')

    # Open the HTML file in the default web browser
    import webbrowser
    webbrowser.open('map.html')
