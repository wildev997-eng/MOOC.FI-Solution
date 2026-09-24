import math

def get_station_data(filename: str):
    with open(filename) as reading:
        stations = {}
        for index in reading:
            index = index.strip()
            spliting = index.split(";")
            if spliting[0] == "Longitude":
                continue
            stations[spliting[3]] = spliting[0:2]
    
    for index, coor in stations.items():
        coor1 = float(coor[0])
        coor2 = float(coor[1])
        stations[index] = (coor1,coor2)   
    return stations

def distance(stations: dict, station1: str, station2: str):
    coor1 = ""
    coor2 = ""
    for data in stations:
        if station1 in data:
            coor1 = stations[data]
        if station2 in data:
            coor2 = stations[data]
    x_km = (coor1[0] - coor2[0]) * 55.26
    y_km = (coor1[1] - coor2[1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    compedium = []
    for index, coor in stations.items():
        for element in stations:
            if element in index:
                continue
            coor1 = stations[index]
            coor2 = stations[element]
            x_km = (coor1[0] - coor2[0]) * 55.26
            y_km = (coor1[1] - coor2[1]) * 111.2
            distance_km = math.sqrt(x_km**2 + y_km**2)
            compedium.append((index,element, distance_km))
    x = 0
    for index in compedium:
        x = max(x, index[2])
    for index in compedium:
        if index[2] == x:
            return index
        


if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)