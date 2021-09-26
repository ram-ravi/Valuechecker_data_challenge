def binary_search(list_of_prefix, country_code):
    """

    :param list_of_prefix: A list contains the prefix code provided by max_value function.
    :param country_code: The (country + area) code obtained from the telephone number using max_value function
    :return: index of the matched (prefix and country + area code) from the list_of_prefix using BS algorithm.
    """

    first = 0
    last = len(list_of_prefix) - 1
    index = -1

    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if list_of_prefix[mid] == country_code:
            index = mid
        else:
            if country_code < list_of_prefix[mid]:
                last = mid - 1
            else:
                first = mid + 1

    if index == -1 and len(str(country_code)) > 1:
        length = len(str(country_code)) - 1
        country_code = int(str(country_code)[:length])
        return binary_search(list_of_prefix, country_code)

    return index


def max_value(sorted_dict, tele_num):
    """

    :param sorted_dict: sorted prefix dictionary that can be further converted into a list for Binary Search Algorithm.
    :param tele_num: telephone number that contains country + area code.
    :return:only the  (country + area) code and the list of prefix as input for BS algorithm.
    """
    max_key_value = max(sorted_dict.keys())
    get_prefix_code = int(str(tele_num)[:len(str(max_key_value))])
    get_prefix_list = list(sorted_dict.keys())

    return get_prefix_code, get_prefix_list


def converter(prefix_dict, phone_num):
    """
    :param prefix_dict: A dictionary with prefix as keys and price as value from the operator dictionary.
    :param phone_num: the telephone number for which the cheapest operator has to be found.
    :return: price of the matched (country + area) code in the telephone number to that of prefix key from
            the prefix dictionary
    """

    sorted_prefix_dict = dict()
    for i in sorted(prefix_dict):
        sorted_prefix_dict[i] = prefix_dict[i]

    prefix_code, prefix_list = max_value(sorted_prefix_dict, phone_num)
    # print(prefix_list)
    # print(prefix_code)
    result = binary_search(prefix_list, prefix_code)
    if result != -1:
        matched_prefix = prefix_list[result]
        price = sorted_prefix_dict[matched_prefix]
        return price


def process(operator_dict, phone_num):
    """
    :param operator_dict: A nested dictionary with operator names as keys and a sub dictionary that contains
                          keys as prefix and prices ($/ min) as values.
    :param phone_num:  The telephone number for which the cheapest operator has to be found.
    :return: The list of cheapest operator(s) for the prefix (country + area) code present in the telephone number.
    """
    price_list = []
    operators = []
    cheap_operator: list[str] = []
    for key, value in operator_dict.items():
        if type(value) is dict:
            temp_price = converter(value, phone_num)
            if temp_price:
                price_list.append(temp_price)
                operators.append(key)

    try:
        min_price = min(price_list)
        min_index = [i for i, x in enumerate(price_list) if x == min_price]
        for index in min_index:
            cheap_operator.append(' '.join([x for i, x in enumerate(operators) if i == index]))
        print('The cheapest amount corresponds to [using binary_search_algorithm]: {} $/min'.format(min_price))
        print(' The cheapest operator(s) is/are given below [using binary_search_algorithm]:')
        print(cheap_operator)
        return cheap_operator

    except ValueError:
        print('NO OPERATOR FOUND FOR THIS NUMBER: %i' % phone_num)
        return 'NO OPERATOR FOUND FOR THIS NUMBER: %i' % phone_num


# Method 2: Finding the cheapest operator using hash tables

def hash_search(prefix_dict, prefix):
    """

    :param prefix_dict: A dictionary with prefix as keys and price as value from the operator dictionary.
    :param prefix: The country + area code obtained from the telephone number
    :return: Returns the price for the matched prefix and (country + area) code.
    """

    price = -1
    if prefix in prefix_dict:
        price = prefix_dict[prefix]
        return price
    elif price == -1 and len(str(prefix)) > 1:
        length = len(str(prefix)) - 1
        prefix_code = int(str(prefix)[:length])
        return hash_search(prefix_dict, prefix_code)
    if price != -1:
        return price


def hash_converter(prefix_dict, phone_num):
    """

    :param prefix_dict:  A dictionary with prefix as keys and price as value from the operator dictionary.
    :param phone_num: The telephone number.
    :return: The price obtained from the hash_search function.
    """

    prefix_code, _ = max_value(prefix_dict, phone_num)
    price = hash_search(prefix_dict, prefix_code)
    return price


def hash_process(operators_dict, phone_num):
    """

    :param operators_dict: A nested dictionary with operator names as keys and a sub dictionary that contains
                          keys as prefix and prices ($/ min) as values.
    :param phone_num: The telephone number.
    :return: The list of cheapest operator(s) found for the (country + area) code in telephone number.
    """

    price_list = []
    operator_list = []
    cheap_operator = []

    for key, value in operators_dict.items():
        temp_price = hash_converter(value, phone_num)
        if temp_price:
            price_list.append(temp_price)
            operator_list.append(key)

    try:
        min_price = min(price_list)
        min_index = [i for i, x in enumerate(price_list) if x == min_price]
        for index in min_index:
            cheap_operator.append(' '.join([x for i, x in enumerate(operator_list) if i == index]))
        print('The cheapest amount corresponds to [using hash_tables]: {} $/min'.format(min_price))
        print('The cheapest operator(s) is/are given below [using hash_tables]:')
        print(cheap_operator)
        return cheap_operator

    except ValueError:
        print('NO OPERATOR FOUND FOR THIS NUMBER: %i' % phone_num)
        return 'NO OPERATOR FOUND FOR THIS NUMBER: %i' % phone_num

# testing our function

# test_operator_dict = {
#     'Operator A': {1: 0.9, 268: 5.1, 46: 0.17, 4620: 0.0, 468: 0.15, 4631: 0.15, 4673: 0.9, 46732: 1.1},
#     'Operator B': {1: 0.92, 44: 0.5, 46: 0.2, 467: 1.1, 48: 1.2}}

# test_tele_num = 46732823704

# process(test_operator_dict, test_tele_num)
