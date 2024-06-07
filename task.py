1.
# https://www.codewars.com/kata/5b047875de4c7f9af800011b/train/python


def sentence(lst):
    key_value_pairs = [(int(list(d.keys())[0]), list(d.values())[0]) for d in lst]
    sorted_pairs = sorted(key_value_pairs)
    sorted_values = [value for key, value in sorted_pairs]
    sentence = ' '.join(sorted_values)

    return sentence


2.
# https://www.codewars.com/kata/5417423f9e2e6c2f040002ae/train/python

def digitize(n):
    digits = [int(i) for i in str(n)]
    return digits


3.
# https://www.codewars.com/kata/59557b2a6e595316ab000046/train/python


def convert_hash_to_array(dct):
    result = [[key, value] for key, value in dct.items()]
    return result


4.
# https://www.codewars.com/kata/53d2697b7152a5e13d000b82/train/python


def copy_list(l):
    if not isinstance(l, list):
        raise TypeError("Input must be a list")
    return l[:]


