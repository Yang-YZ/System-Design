# Mini Datadog

## Description

Datadog is a monitoring service for cloud-scale applications, 
providing monitoring of servers, databases, tools, and services, 
through a SaaS-based data analytics platform.
This is a mini version of Datadog.

## Methods

hit(timestamp) // Records a hit at given timestamp.

get_hit_count_in_last_5_minutes(timestamp) // Gets hit counts in the last 5 minutes.

The two methods will be called with non-descending timestamp (in seconds).

## Example

`Datadog.hit(1)`

`Datadog.hit(2)`

`Datadog.get_hit_count_in_last_5_minutes(3)`

>> 2

`Datadog.hit(300)`

`Datadog.get_hit_count_in_last_5_minutes(300)`

>> 3

`Datadog.get_hit_count_in_last_5_minutes(301)`

>> 2

Read more about [Datadog](https://www.datadoghq.com/).
