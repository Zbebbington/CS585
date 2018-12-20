#to run the code in this file it must be located in the same folder as the files from the textgenrnn
from textgenrnn import textgenrnn

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#use this code to train a new model based on the specified text document
#textgen = textgenrnn()
#textgen.train_from_file('tweets.txt', num_epochs = 5)

#use this code to generate output based on the model created from above
textgen_2 = textgenrnn('textgenrnn_weights.hdf5')
textgen_2.generate(10, temperature = .9)
