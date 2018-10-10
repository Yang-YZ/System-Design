# Geohash

## Description

Geohash is a hash function that convert a location coordinate pair into a base32 string.

This class can convert a (latitude, longitude) pair into a Geohash string, 
and convert a Geohash string to a (latitude, longitude) pair.

## Methods

encode(latitude, longitude, precision) // Takes a (latitude, longitude) pair and returns a Geohash string.
The precision indicates how long the Geohash string would be.

decode(geohash) // Takes a Geohash string and returns a pair of doubles (latitude, longitude).

## Example

`Geohash.encode(39.92816697, 116.38954991, 12)`

>> wx4g0s8q3jf9

`Geohash.decode("wx4g0s")`

>> (39.92706299, 116.39465332)

Read more about [Geohash](https://en.wikipedia.org/wiki/Geohash) or try [Geohash](http://geohash.co/).
