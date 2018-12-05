"""
    fitness_score of text using n-gram statistics (probabilities)
    Used quadgram corpus from Practical Cryptography website by James Lyons which is cited below
    Date: 29th Nov. 2018
"""

from math import log10

class ngram_score(object):
    def __init__(self, ngramfile, sep=' '):
        """
            load a file containing ngrams and counts, calculate log probabilities
        """
        self.ngrams = {}
        for line in open(ngramfile):
            key,count = line.split(sep)
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())
        # calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
            self.floor = log10(0.01/self.N)
    
    def score(self, text):
        """
            compute the score of text
        """
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text) - self.L + 1):
            if text[i:i+self.L] in self.ngrams:
                score += ngrams(text[i:i+self.L])
            else:
                score += self.floor
        return score

"""
    Citation:
        Title: Quadgram Statistics as a Fitness Measure
        Author: James Lyons
        Date: 2009-2012
        Availability: http://practicalcryptography.com
"""
    




    