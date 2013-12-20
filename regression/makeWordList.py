#Use this script tO create feature vectors 
# example: python makeWordList.py WORDS_all-sick.txt trainData.txt testData.txt
 
from tweetReader import *
from utils import *
import sys
import re
import math	


def processFile(filename):
    extra = 0
    users = set() # all users that appear in this file
    print 'Processing file %s' % filename
    reader = tweetReader(filename)
    while True:
        ret = reader.getNextTweet()
        if ret == None:
            break
	#print ret
        (tweet, line) = ret
        users.add(tweet.userName)
	#print tweet.userName
        writeDataForSVM(tweet,filename)
        
def normalizeOrRemoveWord(w):
    w = w.strip('.,;-:"\'?!)(').lower()
    if not(p.match(w)):# and not(w[0] == '#'):
        return None
    return w


def updateUniverseOfWords(relevantTweets):
    """
    Extracts a universe of words that appear in the tweets
    """
    lastLast = last = None
    for tweet in relevantTweets:
        words = tweet.text.split()
        for w in words:
            w = normalizeOrRemoveWord(w)
            if w != None:
                WORDS.add(w)
                if last != None:
                    WORDS.add(tuple(last, w))
                    if lastLast != None:
                        WORDS.add(tuple(lastLast, last, w))
                lastLast = last
                last = w


def readUniverseOfWords(WORDS):
    f_words = open(sys.argv[1], 'r')
    for (idx, w) in enumerate(f_words):
        splitted = w.strip().split(' ')
        if len(splitted) == 1:
            WORDS.append(splitted[0])
        else:
            WORDS.append(tuple(splitted))
        WORDStoID[WORDS[-1]] = idx+1
    f_words.close()
    print 'Number of distinct tokens: %d' % len(WORDS)


def writeUniverseOfWords(WORDS):
    f_words = open(sys.argv[2], 'w')
    for ngram in WORDS:
        if isinstance (ngram, tuple):
            str = ngram.join (' ')
            f_words.write (str)
        else:
            f_words.write (ngram)
            
def filterWords(text):
    """
    Keep only words that pass normalizeOrRemoveWord(), return them as a list
    """
    words = text.split()
    out = []
    for w in words:
        w = normalizeOrRemoveWord(w)
        if w != None:
            out.append(w)
    return out

            
def writeDataForSVM(tweet,filename):
    """
    takes a list of tweet objects and writes a feature representation of each tweet
on a separate line into a file
    """
    #print filename
    global numRelevantTweets

    # Write plain text to a separate file
    text = tweet.text.replace("\r"," ")
    text = text.replace("\n"," ")

    words = filterWords(tweet.text)
    #print(words)
    # single words
    TOKENS = set(words)
    # word pairs
    for i in range(0,len(words)-1):
        TOKENS.add( (words[i], words[i+1]) )
    # word tripples
    for i in range(0,len(words)-2):
        TOKENS.add( (words[i], words[i+1], words[i+2]) )

    #print(TOKENS)
    #print filename
    if filename == 'nyc.trim.liwc.positive':
    	f_features.write('1 ')
    elif filename == 'nyc.trim.liwc.negative':
	f_features.write('-1 ')
    else:
        f_features.write('0 ')

    intersect = TOKENS.intersection(WORDS)
    #print(intersect)
    features = []
    for w in intersect:
        features.append(WORDStoID[w])

    length = len(features)

    if length > 0:
        length = float(1)/math.sqrt(length)
	
    for f in sorted(features):
        f_features.write('%d:%f ' % (f, length ) )
    f_features.write('\n')
    numRelevantTweets += 1

        
           
############################################
# Main
############################################

numRelevantTweets = 0
WORDStoID = {}

p = re.compile('^#*[a-z]+\'*[a-z]*$')
p3 = re.compile('RT[^a-zA-Z0-9]')
filenames = sys.argv[2:]

WORDS = []
readUniverseOfWords(WORDS)
WORDS = frozenset(WORDS)

f_features = open('test_%s_normal.dat' % sys.argv[1], 'w')
for f in filenames:
    processFile(f)
f_features.close()

print 'Number of relevant tweets: %d' % numRelevantTweets

