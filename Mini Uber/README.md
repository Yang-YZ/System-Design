# Mini Uber

## Description

This is a mini version of Uber. It supports two basic Uber features:

1. Drivers report their locations.

2. A Rider requests a uber and gets a matched driver.
When a rider requests a uber, mini Uber matches a closest available driver with the rider, then marks the driver not available.
When next time this matched driver reports location, mini Uber returns with the rider's information.

## Methods

report(driver_id, latitude, longitude) // Return matched trip information; returns None if no matched rider.

request(rider_id, latitude, longitude) // Create a trip with rider's information; find a closest driver, mark this driver not available; 
fill driver_id into this trip; return the trip information.

## Example

`MiniUber.report(1, 36.1344, 77.5672)`
>> None

`MiniUber.report(2, 45.1344, 76.5672)`
>> None

`MiniUber.request(2, 39.1344, 76.5672)`
>> LOG(INFO): Trip(rider_id: 2, driver_id: 1, lat: 39.1344, lng: 76.5672)

`MiniUber.report(1, 38.1344, 75.5672)`
>> LOG(INFO): Trip(rider_id: 2, driver_id: 1, lat: 39.1344, lng: 76.5672)

`MiniUber.report(2, 45.1344, 76.5672)`
>> None

Read more about [Uber](http://eng.uber.com/).
