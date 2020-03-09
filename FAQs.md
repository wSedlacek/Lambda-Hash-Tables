# FAQ

## Table of Contents

- [FAQ](#faq)
  - [Table of Contents](#table-of-contents)
  - [Why do I need to know how a Hash Table works](#why-do-i-need-to-know-how-a-hash-table-works)
  - [What's the difference between a HashTable and a Dictionary](#whats-the-difference-between-a-hashtable-and-a-dictionary)
  - [What's the difference between a HashTable and a Set/HashSet](#whats-the-difference-between-a-hashtable-and-a-sethashset)
  - [What's the difference between a HashTable and a HashMap](#whats-the-difference-between-a-hashtable-and-a-hashmap)
  - [What's the difference between a HashTable and an Object (JavaScript)](#whats-the-difference-between-a-hashtable-and-an-object-javascript)
  - [What's the difference between a HashTable and a Cache](#whats-the-difference-between-a-hashtable-and-a-cache)

<!-- markdownlint-disable MD033 -->

<a name="q100"></a>

<!-- markdownlint-enable MD033 -->

## Why do I need to know how a Hash Table works

Hash tables are preferment, elegant and simple. If you're looking to speed up some code, it's very likely that some form of Hash Table or caching is the answer.

<!-- markdownlint-disable MD033 -->

<a name="q101"></a>

<!-- markdownlint-enable MD033 -->

## What's the difference between a HashTable and a Dictionary

A dictionary is a dynamic HashTable implementation that automatically handles sizing and resizing of the underlying array structure. Dictionaries show up in languages like Python, Java, Swift, Kotlin and more.

<!-- markdownlint-disable MD033 -->

<a name="q102"></a>

<!-- markdownlint-enable MD033 -->

## What's the difference between a HashTable and a Set/HashSet

Sets, sometimes known as HashSets, are HashTable implementations that store data as an unordered collection of keys without values. Sets have the same O(1) insert, delete and search as Hash Tables with no implicit ordering and no duplicates. If you think about how Hash Tables store keys, you'll understand why Sets must be unordered and have no duplicates.

<!-- markdownlint-disable MD033 -->

<a name="q103"></a>

<!-- markdownlint-enable MD033 -->

## What's the difference between a HashTable and a HashMap

HashMaps are dynamic HashTable implementation with some very minor language-specific differences. You can view this (link)[<https://stackoverflow.com/questions/40471/differences-between-hashmap-and-hashtable]> for more details.

<!-- markdownlint-disable MD033 -->

<a name="q104"></a>

<!-- markdownlint-enable MD033 -->

## What's the difference between a HashTable and an Object (JavaScript)

Objects are a JavaScript implementation of a HashTable. Virtually everything in JavaScript is stored as an Object. Closely related to Objects is JSON, or JavaScript Object Notation. This is a text representation of nested Objects and Arrays stored as text. Note that JSON must be Parsed to become an Object, then Stringified to return to a string for transport and storage.

<!-- markdownlint-disable MD033 -->

<a name="q105"></a>

<!-- markdownlint-enable MD033 -->

## What's the difference between a HashTable and a Cache

Cache is just a name for fast data storage. These can take many forms but the most common is key/value storage using a Hash Table.
