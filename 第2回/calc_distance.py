import math
import csv
import pandas as pd

def hav(theta):
    return math.sin(theta/2)**2

#Calculate between 2 points on earth using longtitude and latitude
def calc_distance(location1, location2):
    r = 6378.1
    distance = 2 * r * math.asin(math.sqrt(hav(location2[0]-location1[0]) + math.cos(location1[0]) * math.cos(location2[0]) * hav(location2[1]-location1[1])))

    return distance

def main():
    #Read data from csv file
    loc_df = pd.read_csv('locations.csv')
    #Convert to dictionaty
    loc_dict = loc_df.set_index('name').T.apply(tuple).to_dict()

    #Convert degree to radians
    for k, v in loc_dict.items():
        loc_dict[k] = tuple(map(math.radians, v))

    #Get user's origin and destination input
    origin = input("Please input origin: ")
    destination = input("Please input destination: ")

    #latitude, longtitude of origin and destination
    origin_loc = loc_dict.get(origin, "Does not exist")
    dest_loc = loc_dict.get(destination, "Does not exist")

    print("from: ", origin )
    print("to: ", destination)
    print("distance: ", calc_distance(origin_loc, dest_loc), "km")

if __name__ == '__main__':
    main()
