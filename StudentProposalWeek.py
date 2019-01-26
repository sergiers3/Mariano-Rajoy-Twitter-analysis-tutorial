import json
from collections import Counter
import matplotlib
import nltk
from datetime import datetime
import matplotlib.pyplot as plt

#Create a list of posting dates
datesR = []

#create a list of content:
content = []

#name of the json
fname = 'tweet.json'

with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)

        #get posted date:
        datesR.append(tweet["created_at"])

        # get the content of the tweet :
        content.append(tweet["text"])

# M, T, W, Th, F, S, SU
dayOfWeek = [0, 0, 0, 0, 0, 0, 0]
dayOfWeekName = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Parsed dates:
dates = []

# Parse dates:
for d in datesR:
    datetime_object = datetime.strptime(d, '%a %b %d %H:%M:%S +0000 %Y')
    dates.append(datetime_object)

    # get days of weeks:
    dayOfWeek[datetime_object.weekday()] = dayOfWeek[datetime_object.weekday()] + 1

#set the style
plt.style.use('seaborn-talk')
plt.bar(dayOfWeekName,dayOfWeek, 0.5, align='edge',) # A bar chart

#set labels
plt.xlabel('Days of the week')
plt.ylabel('Number of tweets')

#Rotate the X labels in order to fit them in the graph
plt.xticks(range(len(dayOfWeekName)), dayOfWeekName, rotation=60)
plt.axis('tight')

#force the Y axis to integers
yint = range(0, max(dayOfWeek)+1)
matplotlib.pyplot.yticks(yint)
# Hide the Y labels (note: we do this in order to have a more clear visualization)
plt.yticks([])

#Print the number of tweets in each bar
for a,b in zip(dayOfWeekName, dayOfWeek):
    plt.text(a, b+2, "  "+str(b), color='black', fontweight='bold', fontsize=12, alpha=0.9)

#plt.show()
plt.savefig('nTweetsInWeek.png')# save it on a file