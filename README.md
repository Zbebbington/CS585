# CS585

CODE THAT WE WROTE:

analyze.py 

Contains possible useful functions for analyzing tweets.
i.e. to lowercase, word counts, removes empty tweets, get twitter attributes, etc.

most_freq_plt.py

Test code for getting bag of words data

perplexity.py

A modification of the IBM article ngram model.
used for getting the perplexity for the ngram models.

retrieveTweets.py

Code that helped getting the tweet json file into a text file or csv.

tweet_downloader

Code we wrote using the twitter API to download tweets from users
Prunes out retweets. Max 3200 tweets.
stores in tweets folder. The tweets that we used are in the tweets_to_use folder in the root.

Models we used:

PytorchCharRNN source in folder

TextGenRNN source in folder

Tweet Generator Markov source in folder

bidirectional lstm - too big to upload onto github.

ngram-markov-chars-words https://developer.ibm.com/articles/cc-patterns-artificial-intelligence-part3/

ignore ngram-markov (just a copy of the words folder)

some of the models worked as is with our Twitter data. others we made slight modifications so that we could feed it tweets.
individual readmes will be in model folders
