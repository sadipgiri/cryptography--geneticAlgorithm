"""
    Using Genetic Algorithm (GA) to crack Polyalphabetic Cipher (Vigenere)
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 27th Nov. 2018 
"""

import random
import string
from global_variables import english_language_relative_frequencies, reverse_dict
from cryptography_algebra import relative_frequencies_calculator
from ngram_score import ngram_score
from vigenere_cipher import decrypt
import numpy as np
import pandas as pd

# loading the fitness before calculating fitness_score
fitness = ngram_score('english_quadgrams.txt')

def generate_random_keys(number_of_keys, key_length):
    """
        return list of randomly generated keys using random_key() helper function
    """
    lst = []
    for i in range(number_of_keys):
        lst.append(random_key(key_length))
    return lst

def random_key(key_length):
    """
        using random choice to randomly generate english alphabet
        return randomly generated keyword of size key_length
    """
    key = ''
    for i in range(key_length):
        key = key + random.choice(string.ascii_letters).upper()
    return key

def crossover(parent_1, parent_2):
    """
        get random crossover point
        swap alphabets between two parent keys after the crossover point 
    """
    key_size = len(parent_1)
    crossover_point = random.randint(1, key_size-1)
    child_1 = parent_1[:crossover_point] + parent_2[crossover_point:]
    child_2 = parent_2[:crossover_point] + parent_1[crossover_point:]
    return [child_1, child_2]

def mutation(parent_1, parent_2):
    """
        get two random numbers from parent_1 and parent_2
        swap alphabet indexed at two random numbers between two parents
    """
    key_size = len(parent_1)
    first_random_point  = random.randint(0, key_size-1)
    second_random_point = random.randint(0, key_size-1)
    temp_parent1 = list(parent_1)
    temp_parent2 = list(parent_2)
    temp_parent1[first_random_point] = parent_2[second_random_point]
    temp_parent1[second_random_point] = parent_2[first_random_point]
    temp_parent2[first_random_point] = parent_1[second_random_point]
    temp_parent2[second_random_point] = parent_1[first_random_point]
    return [''.join(temp_parent1), ''.join(temp_parent2)]

def fitness_score(decrypted_text):
    return fitness.score(decrypted_text.replace(' ', '').upper())

def run_genetic_algorithm(key_length, number_of_generations, cipher_text, mutation_rate=0.2):
    """
        initialize by generating random keys with given key length
        sort the random keys
        start the generations (iterations) until the top suited key is returned:
            - apply crossover, mutation, sort top keys
        finally return decrypted text using that top 1 sorted key with highest fitness score
    """
    lst = generate_random_keys(number_of_keys=7000, key_length=key_length)
    sorted_keywords = top_suitable_keywords(number_of_items=600, keywords_with_fitness_scores=keywords_and_suitability_score(lst, cipher_text))
    for m in range(number_of_generations):
        keywords_pairs = pair_keywords(sorted_keywords)
        keywords_pairs = crossover_and_certain_percent_mutation(keywords_pairs,mutation_percent=mutation_rate)
        lst = keywords_pairs.flatten()
        sorted_keywords = top_suitable_keywords(number_of_items=30, keywords_with_fitness_scores=keywords_and_suitability_score(lst, cipher_text))
        print(sorted_keywords)
    return decrypt(cipher_text, keyword=sorted_keywords[0])

def keywords_and_suitability_score(keywords, cipher_text):
    """
        get fitness scores of each keyword
        return two lists with keywords and fitness_scores respectively
        this is for successfully getting top suitable keywords from following mentioned function!
    """
    key_fitness_scores = []
    for i in keywords:
        key_fitness_scores.append(fitness_score(decrypt(ciphertext=cipher_text, keyword=i).upper())) 
    return [keywords, key_fitness_scores]

def top_suitable_keywords(number_of_items, keywords_with_fitness_scores):
    """
        creating pandas dataframe with keywords and fitness_scores column
        return keywords with top fitness_scores
    """
    df = pd.DataFrame(data={'keywords': keywords_with_fitness_scores[0], 'fitness_scores': keywords_with_fitness_scores[1]})
    sorted_df = df.sort_values(by=['fitness_scores'], ascending=False)
    return list(sorted_df['keywords'])[:number_of_items]

def pair_keywords(keywords_list):
    """
        shuffle the list of keywords 
        to randomly pair the keywords
        [could use roulette wheel to pair the keywords!]
    """
    np.random.shuffle(keywords_list)
    return np.array(keywords_list).reshape(int(len(keywords_list)/2), 2)

def crossover_and_certain_percent_mutation(keywords_pairs, mutation_percent):
    """
        applying crossover to keywords_pairs
        applying mutation to certain percent of crossovered children
        this is a helper function for genetic algo function!
    """
    mutation_rate = int(len(keywords_pairs) * mutation_percent)
    for i in keywords_pairs:
        children_after_crossover = crossover(parent_1=i[0], parent_2=i[1])  
        keywords_pairs = np.concatenate((keywords_pairs, np.array([children_after_crossover])), axis=0)
    np.random.shuffle(keywords_pairs)
    for i in range(mutation_rate):
        keywords_pairs[i] = mutation(keywords_pairs[i][0], keywords_pairs[i][1])
    return keywords_pairs

if __name__ == '__main__':
    ft_txt_2 = "FFTWJETYJOTEZMNHSTQLTGJXILFVMBQWNGXXWMNHSFJMMHIBKMMXUHUNQTYBTGNLYHWXRTNGYAJLFFJLNSJTHKJTYNWXRNXMGXWXRHAXIMTFFDJTUEFVJYTKJTHAHANEIMMXWXFKJLJOJKFEXNHARXYATWXHSXNLYHUEFVJMMXHANEIKJGNGYAJITIZEFMNHSTYKFGIHRKJIQTHBSZFGDHSXYANLNLHTQEJWWTSWTFWXUEFVJFJGY"
    web_txt_3 = "WQPZIMKJFRSMQXJKRBHWPJIFZWBYLJHHJJWFNXJKRNAXIKHJBXIATPLYMWXJKRJOX"
    sadip_txt_5 = "SMRLTDOIMKGLXBXGNDTHGNHMSKAFPXDDLVHWRWQDFMHBWGDLNIZESWEMLDBXGNLAIGRHUPANWPTKAPMHAZHIRJEDBJJEPCHLBHZTEOYMSLOPIZWASTPUEIWGWAFPRZIOLIZEUMPJEVMKWRDTHMCKUTLHRLHGNHQHLOSTPUEWPTUHLTSJEQQCLHHXDHUOIIAOQIIJAQLDERHXASCLVVSNBWCWTKQHASFIADEGZPFDRUGWPOIRWMHVI"
    crypto_txt_6 = "CDMSXZQWCKHZWKGDGONJMCXSFJYRAWNUGCLSTKGDGAGKFDWWHKFTICRLJPMWQEGHMCTVKPBBVYCHTAGJGOXOEICPMITVKJLHDVPTFCXVBIHACBCPIZCTCUHFGRAWVVKCBIASTVYGXGGMCGTZULAWFSVYMSLCPVGHMCRCYRXHJVAWBZFICCBBVYCEHDWCYIBCPRRGTBFFKGXDNRAXGUCEWDGSVYGHBGERJAXRTRLSHATVNATQGDCCM"
    hiiamgood_txt_9 = "HUWDQRCTHCWTUFOCBDSAWNQKRGDJPQLPOBGHYBQOZSSHKVLQFFNSDRWCTAFOCBLZBWRQSOWQAPMSMSSGLGMICDKOHXYMUUEZPSULUWVQJHCPHSMABROQHMWZEMIVQKPTLTTKFSDYMAEHKFOOZCKHYKHVRKAWNQOGHRWTICQZVSFOQTDDKBWQAPMPAVIZDAQWNMZFOQKWURQVZOFPVOAZECBHAPQSUYQOOSMLRMTRCPYMXLMISAHUB"
    cryptography_txt_12 = "CDMSXZUWEKVJWKGDGORJOCLCFJYRAWRUICZCTKGDGAKKHDKGHKFTICVLLPAGQEGHMCXVMPPLVYCHTAKJIOLYEICPMIXVMJZRDVPTFCBVDIVKCBCPIZGTEUVPGRAWVVOCDIOCTVYGXGKMEGHJULAWFSZYOSZMPVGHMCVCARLRJVAWBZJIECPLVYCEHDACAIPMPRRGTBJFMGLNNRAXGUGEYDUCVYGHBGIRLALBTRLSHAXVPAHAGDCCM"
    okletsdothisand_txt_14 = "OWZHXDRTXCWDUGWYYEEKRBXLLKAPVSWHBFVSKAQGNZSDSSWAIHALXGPHZKEMHFLGMVZWMNWXELXKDAXZQRENQBPEMMUSFBALBRFOXSOWGHHTICENDVLGXXRFXHKZCUWVOXAWUSTYMKEISBLPLMFVFLBZOQGYYIBKWCISIUEGVONLBDGFXUQFTUSZZTNDDHBVVSTEOXOSFJHDEHKANTOXJSGWWVBZQKCNZVPHKSQRHTZWPYOMPQXFW"
    okletsdothisand_txt_15 = "OWZHXDRTXCWDUGLCXLPLGQSXKASCULZNTRLWUHBVVEEGKCNTJMZHDHWCDAGLCXTWMGUSFHQFTUHGKXILACSTJZWAGXFOXYLLESKLUGVRGHYXEDWDDEHKWFBUSKNLVZLZWAPWRRDFODIOWUOEZCUHZHHRZHLGQSBZBGPYDQOELXUKWEKZWNVQHRPTHHXZTAQGNNWFKYHHEUSISIUIAJOXJSGWWVBZQKCNOZOOVTFGCFYMHLNFSWPRM"
    print(run_genetic_algorithm(key_length=3, number_of_generations=5, cipher_text=web_txt_3))