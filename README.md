# ValueChecker -data challenge

## Routing of telephone calls based on cheapest operator available

This challenge contains two files:

* main.py - The two methods to find the cheapest telephone opreator
* test_main.py - Unit testing for all the functions used in the main.py file

Important things to know:

* operator dictionary: It is a nested dictionary that contains the opreator as  'key' and values contain a dictionary with prefix -(country + area) code as 'key' and price ($/min) as 'value'
* prefix dictionary: The nested dictionary from the opreator dictionary that containes prefix (country + area) code and price ($/min).
* phone_num: The telephone number with (country + area) code.


### Functions to mention:

There are two different main functions used:

* process: The process function is used to obtain the country + area code from the telephone number and match it with the prefix dictionary. The return function provies the cheapest opreator available. It uses Binary Search Algorithm for matching the (country + area) code from phone number with the prefix dictionary.
* hash_process: This function obtains the cheapest operator using HASH table search.


