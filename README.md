# ValueChecker -data challenge

## Routing of telephone calls based on cheapest operator available

### The Challenge:
The goal with this exercise is to write a program that can handle any number of price lists (operators) and then can calculate which operator that is cheapest for a certain number. You can assume that each price list can have thousands of entries but they will all fit together in memory.

Telephone numbers should be inputted in the same format as in price lists, for example “68123456789”. The challenge is to find the cheapest operator for that number.

#### Files present
This solution contains four files:

* main.py - The two methods to find the cheapest telephone opreator
* random_tests.py - A Script that geneartes random sets of opreator dictionary and telephone number to provide as input to the functions.
* unittests_main.py - Unit testing for all the functions used in the main.py file
* multi_process.py - A file that contains multiprocessing method to parallelize the process of obtaining the prices from the dictionary using different cores on the local machine.




#### Workflow
The main workflow for this challenge is shown in the diagram given below:

![pipeline](https://user-images.githubusercontent.com/64869288/134892961-e2e78609-02a8-43ec-8c7f-22ba78f2df08.jpg)


#### Important things to know:

* operator dictionary: It is a nested dictionary that contains the opreators as  'key' and values are a nested dictionary that contains a prefix -(country + area) code as 'key' and price ($/min) as 'value'.
* prefix dictionary: The nested dictionary from the opreator dictionary that containes prefix (country + area) code and price ($/min).
* phone_num: The telephone number with (country + area) code.


#### Functions to mention:

There are two different main functions as shown in the workflow diagram:

* process: 
1. The process function is used to obtain the (country + area) code from the telephone number and match it with the prefix in prefix dictionary.
2. The converter function then calls the Binary search function to find the index at which the prefix is found.
3. In return it (converter function) provies the prices of the matched prefix.
4. The process function then finds the cheapest opreator available from the list of prices obtained. 
5. It uses Binary Search Algorithm for matching the (country + area) code from phone number with the prefix dictionary.

* hash_process: This function uses the same workflow but using HASH table (hash look ups) instead.




