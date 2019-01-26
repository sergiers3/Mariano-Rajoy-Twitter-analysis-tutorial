import json
from collections import Counter
from Lab3.Preprocess import preprocess
import nltk
from nltk.corpus import stopwords
import string
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (6,6)
import matplotlib.pyplot as plt

punctuation = list(string.punctuation)
stop = stopwords.words('spanish') + punctuation + ['rt', 'via', 'RT']

fname = 'tweet.json'
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

        #count_all.update(terms_all)
        #count_all.update(terms_hash)
        count_all.update(terms_only)



plt.style.use('seaborn-talk')

# Set an aspect ratio
width, height = plt.figaspect(1)
fig = plt.figure(figsize=(width,height), dpi=400)

sorted_x, sorted_y = zip(*count_all.most_common(15))

plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='edge')
plt.xticks(range(len(sorted_x)), sorted_x, rotation=60)
plt.axis('tight')
plt.yticks([])

#avoid plot cut off labels
plt.gcf().subplots_adjust(bottom=0.25)

for x in range(len(sorted_x)):
    plt.text(x, sorted_y[x]+1, str(sorted_y[x]), color='black', fontweight='bold', fontsize=10, alpha=0.9)

plt.savefig('termsRajoy.png')# save it on a file
