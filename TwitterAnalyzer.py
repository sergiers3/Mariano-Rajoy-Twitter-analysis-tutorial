import json
import operator
import json
from collections import Counter
from Lab3.Preprocess import preprocess
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords") # download the stopword corpus on our computer
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT']

fname = 'ArtificialIntelligenceTweets.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_hash = [term for term in preprocess(tweet['text'])
                      if term.startswith('#')]
        terms_only = [term for term in preprocess(tweet['text'])
                      if term not in stop and
                      not term.startswith(('#', '@'))]
        terms_all = [term for term in preprocess(tweet['text'])]
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]

        count_all.update(terms_all)
        #count_all.update(terms_hash)
        #count_all.update(terms_only)

    for word, index in count_all.most_common(10):
        print ('%s : %s' % (word, index))