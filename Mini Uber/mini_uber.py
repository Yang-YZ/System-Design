'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):
        # initialize log information.

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper


class MiniUber:

    def __init__(self):
        self.drivers2location = {}
        self.drivers2trip = {}


    def report(self, driver_id, lat, lng):
        # @param {int} driver_id an integer
        # @param {double} lat, lng driver's location
        # return {trip} matched trip information if there have matched rider or null
    
        if driver_id in self.drivers2trip:
            return self.drivers2trip[driver_id] # return matched trip information.
        else:
            self.drivers2location[driver_id] = (lat, lng)
        
        # if no matched rider.
        return None


    def request(self, rider_id, lat, lng):
        # @param rider_id an integer
        # @param lat, lng rider's location
        # return a trip

        # find a closest driver
        closest_driver, closest_dist = None, sys.maxsize
        for driver, location in self.drivers2location.items():
            distance = Helper.get_distance(lat, lng, location[0], location[1])
            if distance < closest_dist:
                closest_driver = driver
                closest_dist = distance

        # create a trip with rider's information.
        trip = Trip(rider_id, lat, lng)
        # fill driver_id into this trip.
        trip.driver_id = closest_driver

        # mark this driver not available.
        del self.drivers2location[closest_driver]
        self.drivers2trip[closest_driver] = trip

        return trip
