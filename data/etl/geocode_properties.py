import pandas as pd
import time
import requests

def geocode(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    response = requests.get(url, params=params, headers={"User-Agent": "FairHouseGeocoder"})
    if response.status_code == 200 and response.json():
        result = response.json()[0]
        return float(result["lat"]), float(result["lon"])
    return None, None

def enrich_with_geolocation():
    df = pd.read_csv("data/raw/sample_properties.csv")
    latitudes = []
    longitudes = []

    for i, row in df.iterrows():
        address = row["address"] + ", " + str(row["zip_code"])
        lat, lon = geocode(address)
        latitudes.append(lat)
        longitudes.append(lon)
        print(f"Geocoded {address} → ({lat}, {lon})")
        time.sleep(1)  # polite delay to avoid rate limit

    df["latitude"] = latitudes
    df["longitude"] = longitudes
    df.to_csv("data/raw/sample_properties_geocoded.csv", index=False)

if __name__ == "__main__":
    enrich_with_geolocation()
