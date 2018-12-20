import json

#sequencer is a map from n grams to probability distribution of next word
#so to get the probability of next word in real sentence find probability in this distribution
#i believe i have the probabilities of each n gram appearing in the data base as of current?
#this is also ignoring the first n-1 words since in this model the sentence starts with a random common n gram
#sentence will be an array of all the words i will need to construct this at some point
#frequencies is from training
def sentencepp(tweet, sequencer, frequencies, n):
    #log each probability then add together in for loop probably
    perplexity = 0.0
    sequence1 = []
    for wd in tweet[(ind - n +1): n-1]:
        sequence1.append(wd)
    #this is for the initial n-1 words
    #this is assuming that frequencies data structure is dictionary
    #also if the word is not in the dictionary not sure how we would want to handle that so leaving that empty for now
    perplexity += math.log(frequencies[sequence1])
    #starting from word n
    for word, ind in tweet[(n-1):], enumerate(tweet, n-1):
        #here iterate through the list given by sequencer
        sequence = []
        for wd in tweet[(ind - n +1): n-1]:
            sequence.append(wd)
        #lst now contains a probability distribution or none
        lst = sequencer.get(sequence)
        #if none then just get probability of word occurring in frequencies
        if lst == None:
            sequence.append(word)
            perplexity += math.log(frequencies[sequence])
        else:
            sequence.append(word)
            #lst can get conditional probability if sum over all possibilities
            wordProb = lst.get(sequence)
            total = 0.0
            for key in lst.keys():
                total += lst.get(key)
            perplexity += math.log(wordProb/total)
    return perplexity

#things worth taking note of
#not sure how to implement end of token yet
#taking the average of all the perplexities of the sentences
def corpuspp(corpus, sequencer, frequencies, n):
    #for each sentence in corpus do sentencepp and then average
    tweet = ""
    perplexity = 0.0
    
    