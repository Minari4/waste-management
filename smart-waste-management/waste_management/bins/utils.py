import requests

def validate_location_with_nominatim(latitude, longitude):
    """
    Validate if the given latitude and longitude correspond to Surigao City using the public Nominatim API.
    """
    # Ensure latitude and longitude are valid
    if latitude is None or longitude is None:
        print("Latitude or longitude is None.")
        return False
    try:
        lat = float(latitude)
        lng = float(longitude)
    except (TypeError, ValueError):
        print("Latitude or longitude is not a valid number.")
        return False

    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lng,
        "format": "json",
        "addressdetails": 1,
    }
    headers = {
        "User-Agent": "SmartWasteManagementApp/1.0 (mark.anthony.alegre05@gmail.com)"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Check if the location corresponds to Surigao City
        if "address" in data and "city" in data["address"]:
            if data["address"]["city"].lower() == "surigao city":
                return True
        return False
    except requests.RequestException as e:
        print(f"Error validating location: {e}")
        return False