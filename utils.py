import requests

def get_distance(frm, to):
    """Takes two points in the form of (lat, lon) and returns the distance and duration between them."""
    url = f"https://router.project-osrm.org/route/v1/driving/{frm[1]},{frm[0]};{to[1]},{to[0]}?overview=false"
    response = requests.get(url)
    data = response.json()
    distance_km = data['routes'][0]['distance'] / 1000  # in km
    duration_h = data['routes'][0]['duration'] / 3600   # in h
    return distance_km, duration_h
