from random import randint
import random
import string
import time
from main import process, hash_process

length = 10

list_dict = []
my_list = []

# Generate random sets of operator dictionary:

for i in range(5):  # list of operators
    my_list.append(f'op {i}')

# Generating pairs of prefix (country + area) code with random phone number.
for _ in range(5):  # no.of operators
    my_dict = {}
    for i in range(10):  # no. of keys in each dictionary
        s = random.randint(1, 100)
        my_dict[s] = random.randint(1, 100)
    list_dict.append(my_dict)

main_dict = dict(zip(my_list, list_dict))  # zip operator dictionary and prefix dictionary together.
result = int(''.join(random.choice(string.digits) for i in range(length)))  # random set of telephone number


# print(main_dict)
# print(result)


def timer(fun):
    start = time.time()
    fun(main_dict, result)
    end = time.time()
    dur = round(end - start, ndigits=10)
    print(dur)


# timer(process)    # using the process function from the main.py file

# timer(hash_process)  # using the hash_process function from the main.py file
