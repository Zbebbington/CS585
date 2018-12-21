import sys
import json
import string
import random
import csv
import math

POPULAR_NGRAM_COUNT = 10000
#Population is all the possible items that can be generated
population = ' ' + string.ascii_lowercase

def preprocess_frequencies(frequencies, order):
    '''Compile simple mapping from N-grams to frequencies into data structures to help compute
    the probability of state transitions to complete an N-gram
    Arguments:
        frequencies -- mapping from N-gram to frequency recorded in the training text
        order -- The N in each N-gram (i.e. number of items)
    Returns:
        sequencer -- Set of mappings from each N-1 sequence to the frequency of possible
            items completing it
        popular_ngrams -- list of most common N-grams
    '''
    #print(type(list(frequencies.keys())[0]))
    sequencer = {}
    ngrams_sorted_by_freq = [
        k for k in sorted(frequencies, key=frequencies.get, reverse=True)
    ]
    popular_ngrams = ngrams_sorted_by_freq[:POPULAR_NGRAM_COUNT]
    for ngram in frequencies:
        #Separate the N-1 lead of each N-gram from its item completions
        freq = frequencies[ngram]
        lead = ngram[:-1]
        final = ngram[-1]
        sequencer.setdefault(lead, {})
        sequencer[lead][final] = freq
    return sequencer, frequencies, popular_ngrams


def generate_letters(corpus, frequencies, sequencer, popular_ngrams, length, order):
    '''Generate text based on probabilities derived from statistics for initializing
    and continuing sequences of letters
    Arguments:
        sequencer -- mapping from each leading sequence to frequencies of the next letter
        popular_ngrams -- list of the highest frequency N-Grams
        length -- approximate number of characters to generate before ending the program
        order -- The N in each N-gram (i.e. number of items)
    Returns:
        nothing
    '''
    #The lead is the initial part of the N-Gram to be completed, of length N-1
    #containing the last N-1 items produced
    lead = ''
    #Keep track of how many items have been generated
    generated_count = 0
    out = ''
    #while generated_count < length:
        #This condition will be true until the initial lead N-gram is constructed
        #It will also be true if we get to a dead end where there are no stats
        #For the next item from the current lead
    #    if lead not in sequencer:
     #       #Pick an N-gram at random from the most popular
     #       reset = random.choice(popular_ngrams)
      #      #Drop the final item so that lead is N-1
     #       lead = reset[:-1]
      #      for item in lead:
      #          #print(item, end='', flush=True)
       #         out += item
     #       generated_count += len(lead) + 1
       # else:
         #   freq = sequencer[lead]
         #   weights = [ freq.get(c, 0) for c in population ]
          #  chosen = random.choices(population, weights=weights)[0]
            #print(chosen + ' ', end='', flush=True)
            #Clip the first item from the lead and tack on the new item
           # lead = lead[1:]+ chosen
           # generated_count += 2
            #out += chosen + ' '
    #print(out)
    perplexity = corpuspp(corpus, sequencer, frequencies, order)
    print(abs(perplexity))
    return out

    #sequencer is a map from n grams to probability distribution of next word
#so to get the probability of next word in real sentence find probability in this distribution
#i believe i have the probabilities of each n gram appearing in the data base as of current?
#this is also ignoring the first n-1 words since in this model the sentence starts with a random common n gram
#sentence will be an array of all the words i will need to construct this at some point
#frequencies is from training
def sentencepp(tweet, sequencer, frequencies, n, totalNgrams):
    #log each probability then add together in for loop probably
    perplexity = 0.0
    sequence1 = ""
    for wd in tweet[0: n-1]:
        sequence1 = sequence1 + wd
    #this is for the initial n-1 words
    #this is assuming that frequencies data structure is dictionary
    #also if the word is not in the dictionary not sure how we would want to handle that so leaving that empty for now
    if(frequencies.get(sequence1) == None):
        perplexity += math.log(1/totalNgrams)
    else:
        perplexity += math.log(frequencies[sequence1])
    #starting from word n
    ind = n -1
    for word in tweet[(n-1):]:
        #here iterate through the list given by sequencer
        sequence = ""
        for wd in tweet[(ind - n +1): n-1]:
            sequence = sequence + wd
        #lst now contains a probability distribution or none
        lst = sequencer.get(sequence)
        #if none then just get probability of word occurring in frequencies
        if lst == None:
            #since this model will output a popular word when it encounters a ngram it never saw before we're going to assume probability
            #of getting this word that might not be in popular ngrams to be basically a very small number so perplexity isn't 0
            perplexity += math.log(1/totalNgrams)
        else:
            sequence = sequence + word
        #lst can get conditional probability if sum over all possibilities
            wordProb = lst.get(sequence)
            if(wordProb == None):
                perplexity += math.log(1/totalNgrams)
            else:
                total = 0.0
                for key in lst.keys():
                    total += lst.get(key)
                perplexity += math.log(wordProb/total)
        ind = ind + 1
    return perplexity

#things worth taking note of
#not sure how to implement end of token yet
#taking the average of all the perplexities of the sentences
def corpuspp(corpus, sequencer, frequencies, n):
    #for each sentence in corpus do sentencepp and then average
    perplexity = 0.0
    #not really possible to backtrack to get total number of ngrams
    totalNgrams = 100000000

    #if read file outside of this function then replace lines with corpus and remove the next line
    with open('tweets.txt', encoding='utf-8', errors='ignore') as f:
        lines = f.read().splitlines()
    for line in lines:
        perplexity += sentencepp(line, sequencer, frequencies, n, totalNgrams)
    perplexity = perplexity/len(lines)
    return perplexity


if __name__ == '__main__':
    #File with N-gram frequencies is the first argument
    gram = 7
    open_file = str(gram) + 'GramFreq.json'
    raw_freq_fp = open(open_file)
    length = 280
    raw_freqs = json.load(raw_freq_fp)

    #Figure out the N-gram order.Just pull the first N-gram and check its length
    order = len(next(iter(raw_freqs)))
    sequencer, frequencies, popular_ngrams = preprocess_frequencies(raw_freqs, order)
    corpus = sys.argv[1]
    generate_letters(corpus, frequencies, sequencer, popular_ngrams, length, order)