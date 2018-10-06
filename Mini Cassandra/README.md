# Mini Cassandra

## Description

This is a mini version of Cassandra.
Cassandra is a NoSQL storage. The structure has two-level keys that map to a value.

1. row_key.
The row_key is also known as hash_key, shard_key or partition key, which determines where the data is stored in the cluster.
The row_key is used to hash and can not support range query. Simplify row key to be a string.

2. column_key.
The column_key is sorted and support range query. Simplify column key to be an integer.

3. value.
The value is a string. You can serialize any data into a string and store it in value.

## Methods

insert(row_key, column_key, value) // Adds an element value at the specified position.

query(row_key, column_start, column_end) // Return a list of elements at the specified row, and column range.

## Example

`Cassandra.insert("google", 1, "hello")`

`Cassandra.query("google", 0, 1)`
>> [(1, "hello")]

Read more about [Cassandra](http://cassandra.apache.org/).
