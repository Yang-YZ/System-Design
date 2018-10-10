
#Decimal  | 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#Base 32  | 0 1 2 3 4 5 6 7 8 9  b  c  d  e  f  g
 
#Decimal  | 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
#Base 32  |  h  j  k  m  n  p  q  r  s  t  u  v  w  x  y  z

DECIMAL2BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"

class GeoHash:

    def encode(self, latitude, longitude, precision):
        """
        @param: latitude: one of a location coordinate pair 
        @param: longitude: one of a location coordinate pair 
        @param: precision: an integer between 1 to 12
        @return: a base32 string
        """
        binary = []
        left_lng, right_lng, left_lat, right_lat = -180, 180, -90, 90
        while len(binary) < precision * 5:
            digit, left_lng, right_lng = self.generate_binary(longitude, left_lng, right_lng)
            binary.append(digit)
            digit, left_lat, right_lat = self.generate_binary(latitude, left_lat, right_lat)
            binary.append(digit)

        geohash = ""
        for i in range(0, precision * 5, 5):
            geohash += self.binary2base32(binary[i:i + 5])
        
        return geohash
        
        
    def generate_binary(self, value, left_range, right_range):
        mid = (left_range + right_range) / 2
        if value > mid:
            return (1, mid, right_range)
        else:
            return (0, left_range, mid)


    def binary2base32(self, binary):
        decimal = 0
        for index, digit in enumerate(reversed(binary)):
            decimal += digit * (2 ** index)
        return DECIMAL2BASE32[decimal]


    def decode(self, geohash):
        """
        @param: geohash: geohash a base32 string
        @return: latitude and longitude a location coordinate pair
        """
        binary = []
        for base in geohash:
            binary += self.decimal_to_binary(DECIMAL2BASE32.find(base))
        #print (binary)
        odd = [binary[i] for i in range(0, len(binary), 2)]
        even = [binary[i] for i in range(1, len(binary), 2)]
        
        longitude = self.get_location(-180, 180, odd)
        latitude = self.get_location(-90, 90, even)
        
        return (latitude, longitude)


    def get_location(self, left, right, binary):
        for digit in binary:
            mid = (left + right) / 2
            if digit == 1:
                left = mid
            else:
                right = mid
        return (left + right) / 2


    def decimal_to_binary(self, decimal):
        binary = [0] * 5
        index = 4
        while decimal > 0 and index >= 0:
            if decimal % 2 == 0:
                binary[index] = 0
            else:
                binary[index] = 1
            decimal //= 2
            index -= 1
        
        return binary
