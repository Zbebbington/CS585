#sequencer is a map from n grams to probability distribution of next word
#so to get the probability of next word in real sentence find probability in this distribution
#i believe i have the probabilities of each n gram appearing in the data base as of current?
#this is also ignoring the first n-1 words since in this model the sentence starts with a random common n gram
#sentence will be an array of all the words i will need to construct this at some point
#frequencies is from training
def sentencepp(sentence, sequencer, frequencies, n):
    #log each probability then add together in for loop probably
    perplexity = 0.0
    for word in sentence[:(n-1)]:
        #this is for the initial n-1 words
        #this is assuming that frequencies data structure is dictionary
        #also if the word is not in the dictionary not sure how we would want to handle that so leaving that empty for now
        perplexity += math.log(frequencies[word])
    #starting from word n
    for word, ind in sentence[(n-1):], enumerate(sentence, n-1):
        #here iterate through the list given by sequencer
        sequence = []
        for wd in sentence[(ind - n +1): n-1]:
            sequence.append(wd)
        #lst now contains a probability distribution
        lst = sequencer(sequence)
        #not entirely sure how sequencer stores information
        wordProb = lst.
        perplexity += math.log(wordProb)

#things worth taking note of
#not sure how to implement end of token yet
#taking the average of all the perplexities of the sentences
def corpuspp(corpus, sequencer, frequencies, n):
    #for each sentence in corpus do sentencepp and then average
    sentence = ""
    perplexity = 0.0
    
    