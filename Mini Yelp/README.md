# Mini Yelp

## Description

This is a mini version of Yelp. It supports three basic Yelp features:

1. Add a restaurant with its name and location.

2. Remove a restaurant with id.

3. Given a user's location, search the nearby restaurants within k miles.
A location is represented by latitude and longitude, both in double.
If there are more than one nearby restaurant, the search result would be in ascending order of the distance between the user and restaurants.

## Methods

add_restaurant(name, location) // Add a restaurant with its name and location to the system.

remove_restaurant(restaurant_id) // Remove a restaurant with restaurant_id.

neighbors(location, k) // Find nearby restaurants within k miles.

## Example

`MiniYelp.add_restaurant("Central Perk", 10.4999999, 11.599999)`
>> 1

`MiniYelp.add_restaurant("Ding Tai Feng", 3.4999999, 11.512109)`
>> 2

`MiniYelp.neighbors(10.5, 11.6, 7.0)`  // The distance between location(10.5, 11.6) and "Central Perk" is almost 0.
>> ["Central Perk"]

`MiniYelp.remove_restaurant(1) `
>> None

`MiniYelp.neighbors(10.5, 11.6, 7.0)`  // The distance between location(10.5, 11.6) and "Ding Tai Feng" is 7.0005517 miles > 7.0 miles.
>> []

Read more about [Yelp](https://www.yelp.com/).
 


