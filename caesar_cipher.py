"""
    encrypt and decrypt Caesar Cipher
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 3rd Nov. 2018
"""

import numpy as np
from cryptography_algebra import convert_np_array_numbers_to_sentence, convert_sentence_to_np_array_of_numbers
from genetic_algorithm import fitness_score

def encrypt(plaintext, key):
    """
        convert plaintext to numpy array with numbers
        shift numbers using caesar cipher key
        return upper case ciphertext after converting numpy numbers into sentence
    """
    plaintext_in_numbers = convert_sentence_to_np_array_of_numbers(plaintext)
    caesar_shifted = (plaintext_in_numbers + key) % 26
    return convert_np_array_numbers_to_sentence(caesar_shifted).upper()

def decrypt(ciphertext, key):
    """
        convert convert ciphertext to numpy array with numbers
        reverse caesar shift with the key
        return plaintext after converting caesar shifted into sentence
    """
    ciphertext_in_numbers = convert_sentence_to_np_array_of_numbers(ciphertext)
    caesar_shifted = (ciphertext_in_numbers - key) % 26
    return convert_np_array_numbers_to_sentence(caesar_shifted)

def crack(cipher_text):
    """
    Using fitness function from GA to crack caesar and give very suited key!
        get fitness score of all 25 keys (applying fitness function after decrypting caesar shift using those keys)
        find the index (i) of that top fitted key
        return the key and decrypted message using that key matching that index (i) on keys
    """
    fitnesses = []
    keys = []
    for i in range(26):
        keys.append(i)
        fitnesses.append(fitness_score(decrypt(cipher_text, i)))
    key = keys[fitnesses.index(max(fitnesses))]
    return [decrypt(cipher_text,key), key]

if __name__ == '__main__':
    encrypted_text = encrypt("hi i am sadip", 10)
    print(crack(encrypted_text))