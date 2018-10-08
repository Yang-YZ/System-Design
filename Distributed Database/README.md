# Bloom Filter

## Description

This is a mini version of standard bloom filter, that supports the following methods.

## Methods

BloomFilter(k) // The constructor creates k hash functions.

add(string) // Add a string into bloom filter.

contains(string) // Check whether a string exists in bloom filter.

remove(string) // Remove a string from bloom filter.

## Example

`BloomFilter(3)`

`add("hello")`

`add("world")`

`contains("hello")`

>> True

`remove("hello")`

`contains("hello")`

>> False

`contains("world")`

>> True

Read more about [Bloom Filter](https://en.wikipedia.org/wiki/Bloom_filter).
