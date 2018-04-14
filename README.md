WhatYear
--------

A small script written using only native modules in python2/3 that returns a matching
list of years that such a date can exist on. It's built with heavy input cleaning, so
it will allow you to use the minimum non-ambiguous strings to represent the date.

For example:

<code>./whatyear.py friday 13 september

For the day Friday, 13 September:

Matching years: [2013, 2002, 1996, 1991, 1985, 1974, 1968, 1963, 1957, 1946] </code>

<code>./whatyear.py thurs 13 a

Month ambiguous. Could be ['April', 'August'] </code>

<code>./whatyear.py t 25 jul

Weekday ambiguous. Could be ['Tuesday', 'Thursday'] </code>

<code>./whatyear.py tu 31 jun

Month day not in range: [1,30] </code>

<code>./whatyear.py thurs 13 april

For the day Thursday, 13 April:

Matching years: [2017, 2006, 2000, 1995, 1989, 1978, 1972, 1967, 1961, 1950] </code>

<code>./whatyear.py F 29 Feb

For the day Friday, 29 February:

Matching years: [2008, 1980, 1952, 1924, 1884, 1856, 1828, 1788, 1760, 1732] </code>
