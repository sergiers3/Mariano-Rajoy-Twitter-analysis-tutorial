import json
from collections import Counter
import matplotlib
from datetime import datetime
import matplotlib.pyplot as plt

#Create a list of posting dates
datesR = []

#create a list of content:
content = []

#name of the Json
fname = 'tweet.json'

with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)

        #get posted date:
        datesR.append(tweet["created_at"])

        # get the content of the tweet :
        content.append(tweet["text"])

# Parsed dates:
dates = []

#hours of tweets:
hours = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Parse dates:
for d in datesR:
    datetime_object = datetime.strptime(d, '%a %b %d %H:%M:%S +0000 %Y')
    dates.append(datetime_object)

    # get the hours
    hours[datetime_object.hour] = hours[datetime_object.hour] + 1

# List of the names for the X axis
xNames = ['00h','01h','02h','03h','04h','05h','06h','07h','08h','09h','10h','11h','12h','13h','14h','15h','16h','17h','18h','19h','20h','21h','22h','23h']

#set the style
plt.style.use('seaborn-talk')
plt.bar(xNames,hours, 1, align='edge',) # A bar chart

#set labels
plt.xlabel('Hours of the day')
plt.ylabel('Number of tweets')

#Rotate the X labels in order to fit them in the graph
plt.xticks(range(len(xNames)), xNames, rotation=60)
plt.axis('tight')

#force the Y axis to integers
yint = range(0, max(hours)+1)
matplotlib.pyplot.yticks(yint)
# Hide the Y labels (note: we do this in order to have a more clear visualization)
plt.yticks([])

#Print the number of tweets in each bar
for a,b in zip(xNames, hours):
    plt.text(a, b+1, str(b), color='black', fontweight='bold', fontsize=10, alpha=0.9)

#plt.show()
plt.savefig('nTweetsInday.png')# save it on a file