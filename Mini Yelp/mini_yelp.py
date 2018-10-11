'''
Definition of Location:
class Location:
    # @param {double} latitude, longitude
    # @param {Location}
    @classmethod
    def create(cls, latitude, longitude):
        # This will create a new location object

Definition of Restaurant:
class Restaurant:
    # @param {str} name
    # @param {Location} location
    # @return {Restaurant}
    @classmethod
    def create(cls, name, location):
        # This will create a new restaurant object,
        # and auto fill id

Definition of Helper
class Helper:
    # @param {Location} location1, location2
    @classmethod
    def get_distance(cls, location1, location2):
        # return calculate the distance between two location

Definition of GeoHash
class GeoHash:
    # @param {Location} location
    # @return a string
    @classmethom
    def encode(cls, location):
        # return convert location to a geohash string
    
    # @param {str} hashcode
    # @return {Location}
    @classmethod
    def decode(cls, hashcode):
        # return convert a geohash string to location
'''
from YelpHelper import Location, Restaurant, GeoHash, Helper


class MiniYelp:

    def __init__(self):
        # TODO: balanced BST
        self.restaurants = {}
        self.count = 1


    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        self.restaurants[self.count] = Restaurant.create(name, location)
        self.count += 1
        return self.count - 1


    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        if restaurant_id <= self.count:
            del self.restaurants[restaurant_id]
            # self.count -= 1
        else:
            print("This restaurant is not in Yelp.")


    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by 
    # distance from near to far.
    def neighbors(self, location, k):
        neighbors = []
        for id, restaurant in self.restaurants.items():
            distance = Helper.get_distance(restaurant.location, location)
            if distance < k:
                neighbors.append([distance, restaurant.name])
        
        # sort by distance
        neighbors = sorted(neighbors, key=lambda obj: obj[0])
        return [name for dist, name in neighbors]
