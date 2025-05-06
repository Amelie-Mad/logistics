import requests
import numpy as np

def get_distance(frm, to):
    """Takes two points in the form of (lat, lon) and returns the distance and duration between them."""
    url = f"https://router.project-osrm.org/route/v1/driving/{frm[1]},{frm[0]};{to[1]},{to[0]}?overview=false"
    response = requests.get(url)
    data = response.json()
    distance_km = data['routes'][0]['distance'] / 1000  # in km
    duration_h = data['routes'][0]['duration'] / 3600   # in h
    return distance_km, duration_h

def distance_time_matrix(depot, clients, sample_size = 3):
    """
    Function to calculate the distance and time matrix between the depot and clients
    depot: tuple / list with the coordinates of the depot
    clients: array with the coordinates of the clients as tuples / lists
    sample_size: number of clients to sample from the list of clients
    """
    clients_sample = clients[:sample_size]
    locations = np.vstack([depot, clients_sample])

    distance_matrix = np.zeros((len(locations), len(locations)))
    time_matrix = np.zeros((len(locations), len(locations)))

    for i in range(len(locations)):
        for j in range(len(locations)):
            dist, time = get_distance(locations[i], locations[j])
            distance_matrix[i, j] = dist
            time_matrix[i, j] = time
    return distance_matrix, time_matrix
