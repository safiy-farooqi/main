import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env.local
load_dotenv(".env.local")

def find_restaurants(api_key, location, radius, cuisine_type):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": int(radius),  # Convert to integer, assuming the input is valid
        "type": "restaurant",
        "keyword": cuisine_type,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    results = response.json().get("results", [])

    restaurants = []
    for place in results:
        name = place.get("name", "N/A")
        address = place.get("vicinity", "N/A")
        restaurants.append({"name": name, "address": address})
    return restaurants

def main():
    api_key = os.getenv("API_KEY")  # Get API key from .env.local file
    if not api_key:
        print("API key not found. Please check your .env.local file.")
        return

    print("Please enter your location in the format latitude,longitude (e.g., 35.9027,-79.0451):")
    location = input()

    print("Enter the search radius in miles:")
    radius = float(input()) * 1609.34  # Assuming input is always valid

    print("Enter the cuisine type:")
    cuisine_type = input()

    restaurants = find_restaurants(api_key, location, radius, cuisine_type)

    if restaurants:
        for restaurant in restaurants:
            print(f"{restaurant['name']} - {restaurant['address']}")
    else:
        print("No restaurants found or error in fetching data.")

if __name__ == "__main__":
    main()

