from typing import List


def max_value(sorted_dict, tele_num):
    max_key_value = max(sorted_dict.keys())
    get_prefix_code = int(str(tele_num)[:len(str(max_key_value))])
    get_prefix_list = list(sorted_dict.keys())

    return get_prefix_code, get_prefix_list


def binary_search(list_of_prefix, country_code):
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


def converter(prefix_dict, phone_num):
    sorted_prefix_dict = dict()
    for i in sorted(prefix_dict):
        sorted_prefix_dict[i] = prefix_dict[i]

    prefix_code, prefix_list = max_value(sorted_prefix_dict, phone_num)
    # print(lis)
    # print(num)
    result = binary_search(prefix_list, prefix_code)
    if result != -1:
        matched_prefix = prefix_list[result]
        price = sorted_prefix_dict[matched_prefix]
        return price


def process(operator_dict, phone_num):
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
        print(' The cheapest operators is/are given below [using binary_search_algorithm]:')
        print(cheap_operator)
        return cheap_operator

    except ValueError:
        print('NO OPERATOR FOUND FOR THIS NUMBER: %i'%(phone_num))
        return 'NO OPERATOR FOUND FOR THIS NUMBER: %i'%(phone_num)


# hash table

def hash_search(prefix_dict, prefix_code):
    price = -1
    if prefix_code in prefix_dict:
        price = prefix_dict[prefix_code]
        return price
    elif price == -1 and len(str(prefix_code)) > 1:
        length = len(str(prefix_code)) - 1
        prefix_code = int(str(prefix_code)[:length])
        return hash_search(prefix_dict, prefix_code)
    if price != -1:
        return price


def hash_converter(prefix_dict, phone_num):
    prefix_code, _ = max_value(prefix_dict, phone_num)
    price = hash_search(prefix_dict, prefix_code)
    return price


def hash_process(operators_dict, phone_num):
    price = []
    operator = []
    cheap_operator = []
    for key, value in operators_dict.items():
        if type(value) is dict:
            temp_price = hash_converter(value, phone_num)
            if temp_price:
                price.append(temp_price)
                operator.append(key)

    try:
        min_price = min(price)
        min_index = [i for i, x in enumerate(price) if x == min_price]
        for index in min_index:
            cheap_operator.append(' '.join([x for i, x in enumerate(operator) if i == index]))
        print('The cheapest amount corresponds to [using hash_tables]: {} $/min'.format(min_price))
        print('The cheapest operators is/are given below [using hash_tables]:')
        print(cheap_operator)
        return cheap_operator
    except ValueError:
        print('NO OPERATOR FOUND FOR THIS NUMBER: %i'%(phone_num))
        return 'NO OPERATOR FOUND FOR THIS NUMBER: %i'%(phone_num)


