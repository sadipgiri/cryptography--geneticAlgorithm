"""
    cryptography algebra is a helper python3 program to count frequencies of alphabets, calculate index of coincidence, guess length of Vigenere cipher keyword
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 31th Oct. 2018
"""

from global_variables import eng_alphabets, alphabets_to_values, values_to_alphabets
import numpy as np
import sys

def freq_count(sentence):
    '''
        convert all alphabets of a sentence to lowercase letter
        count each of them in the sentence
        make a dictionary of alphabets with frequencies 
    '''
    freq_dict = {}
    lower_case_sentence = sentence.lower()
    for i in eng_alphabets:
        freq_dict[i] = lower_case_sentence.count(i)
    return freq_dict

def calc_index_of_coincidence(cipher_text):
    """
        get all the frequencies from cipher_text
        convert it to numpy array for faster computation using Vectorization technique
        formulae: summation[(n(i)(n(i) - 1))/n(n - 1)]
            where, n(i) is frequency of each alphabet e.g. n(a) = 5, n(b) = 8..
                   n is total frequency
    """
    freqs = freq_count(cipher_text)
    numpy_arr = np.array(list(freqs.values()))
    n = sum(numpy_arr)
    return (sum((numpy_arr * (numpy_arr - 1)))/(n * (n - 1)), n)

def guess_vigenere_length_of_keyword(cipher_text):
    """
        get IOC (index of coincidence of cipher text) and total frequency
        use formulae to return length of keyword of vigenere
            formula: guessed_length = (0.027 * n)/((n - 1)*IOC + 0.065 - 0.038 * n)
            where, n is total frequency and IOC is index of coincidence
    """
    n_and_IOC = calc_index_of_coincidence(cipher_text)
    IOC = n_and_IOC[0]
    n = n_and_IOC[1]
    return int((0.027 * n)/((n - 1)*IOC + 0.065 - 0.038 * n))

def convert_sentence_to_np_array_of_numbers(sentence):
    """
        convert sentence to lowercase
        check if every character of sentence is english alphabet
        if so, convert alphabet to number and append to numpy array and return numpy array
    """
    cipher_in_numbers_lst = []
    for i in sentence.lower():
        if i in eng_alphabets:
            cipher_in_numbers_lst.append(alphabets_to_values[i])
    return np.array(cipher_in_numbers_lst)

def convert_np_array_numbers_to_sentence(array):
    """
        convert each number of numpy array to english alphabet 
        add those alphabets and return whole sentence
    """
    sentence = ""
    for i in array:
        sentence = sentence + values_to_alphabets[i]
    return sentence

def maintain_length_of_keyword_with_plaintext(plaintext, keyword):
    """
        get the length of plaintext and keyword
        maintain same keyword length to plaintext using divisor and remainder (modulus)
        return extended keyword to easily excrypt and decrypt Vigenere cipher
    """
    extended_keyword = ""
    key_length = len(keyword)
    text_length = len(filter_sentence(plaintext))
    divisor = int(text_length/key_length)
    remainder = text_length % key_length
    for i in range(divisor):
        extended_keyword = extended_keyword + keyword
    return extended_keyword + extended_keyword[0:remainder]

def filter_sentence(sentence):
    """
        check each character of sentence with our english alphabet dictionary
        return filtered sentence
    """
    sent = ""
    for i in sentence.lower():
        if i in eng_alphabets:
            sent = sent + i
    return sent

def relative_frequencies_calculator(decrypted_message):
    """
        get frequencies of alphabets in decrypted message
        count total frequency (n)
        and calculate relative freq using formula: freq.(i)/n 
    """
    freq_dict = freq_count(decrypted_message)
    total_freq = sum(freq_dict.values())
    for i in freq_dict:
        freq_dict[i] = freq_dict[i]/total_freq
    return freq_dict
    
if __name__ == '__main__':
    txt = "vptnvffuntshtarptymjwzirappljmhhqvsubwlzzygvtyitarptyiougxiuydtgzhhvvmumshwkzgstfmekvmpkswdgbilvjljmglmjfqwioiivknulvvfemioiemojtywdsajtwmtcgluysdsumfbieugmvalvxkjduetukatymvkqzhvqvgvptytjwwldyeevquhlulwpkt"
    print(guess_vigenere_length_of_keyword(txt))