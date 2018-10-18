# Rate Limiter

## Description

This is a mini version of rate limiters.
Rate limiter is used to control the rate of traffic sent or received by a network interface controller 
and is used to prevent responding to a lot of requests.

## Methods

is_ratelimited(timestamp, event, rate, increment) // Return True or False to indicate the event is limited or not.

timestamp: The current timestamp, which is an integer and in second unit.

event: The string to distinct different event. For example, "login" or "signup".

rate: The rate of the limit. 1/s (1 time per second), 2/m (2 times per minute), 10/h (10 times per hour), 100/d (100 times per day). 
The format is [integer]/[s/m/h/d] as a string.

increment: Whether we should increase the counter (or take this call as a hit of the given event). 

## Example

`RateLimiter.is_ratelimited(1, "login", "3/m", true)`

>> False

`RateLimiter.is_ratelimited(11, "login", "3/m", true)`

>> False

`RateLimiter.is_ratelimited(21, "login", "3/m", true)`

>> False

`RateLimiter.is_ratelimited(30, "login", "3/m", true)`

>> True

`RateLimiter.is_ratelimited(65, "login", "3/m", true)`

>> False

`RateLimiter.is_ratelimited(300, "login", "3/m", true)`

>> False

Read more about [Rate Limiter](https://en.wikipedia.org/wiki/Rate_limiting).
