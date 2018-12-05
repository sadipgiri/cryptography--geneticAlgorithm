eng_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabets_to_values = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}

# used reverse_dict helper function to reverse the dictionary
values_to_alphabets = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'
}

english_language_relative_frequencies = {
    'e': 0.1202,
    't': 0.091,
    'a': 0.0812,
    'o': 0.0768,
    'i': 0.0731,
    'n': 0.0695,
    's': 0.06280000000000001,
    'r': 0.0602,
    'h': 0.0592,
    'd': 0.0432,
    'l': 0.0398,
    'u': 0.0288,
    'c': 0.0271,
    'm': 0.026099999999999998,
    'f': 0.023,
    'y': 0.021099999999999997,
    'w': 0.0209,
    'g': 0.0203,
    'p': 0.0182,
    'b': 0.0149,
    'v': 0.0111,
    'k': 0.0069,
    'x': 0.0017000000000000001,
    'q': 0.0011,
    'j': 0.001,
    'z': 0.0007000000000000001,
}

# helper function to reverse a dictionary
def reverse_dict(dct):
    return dict([reversed(i) for i in dct.items()])

if __name__ == '__main__':
    d = alphabets_to_values
    reverse = reverse_dict(d)
    print(reverse)
    print(sum(english_language_relative_frequencies.values()))