## using multiprocessing


import random
import string
import time
from functools import partial
from multiprocessing import Pool

import main

# Random sets of dictionary to provide as input to the converter
list_dict = []
for _ in range(5):  # no.of operators
    my_dict = {}
    for i in range(5):  # no. of keys in each dictionary
        s = random.randint(1, 10)
        my_dict[s] = random.randint(1, 10)
    list_dict.append(my_dict)

tele = int(''.join(random.choice(string.digits) for i in range(8)))

if __name__ == '__main__':
    t1 = time.perf_counter()
    pool = Pool()
    prices = pool.map(partial(main.hash_converter, phone_num=tele), list_dict)
    print(list_dict)
    print(tele)
    print(prices)

    t2 = time.perf_counter()

    print(f'Finished in {t2 - t1} seconds')
    pool.terminate()
