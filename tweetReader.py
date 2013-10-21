from __future__ import print_function
from Tweet import *
import re
import simplejson as json
from datetime import datetime, timedelta
import sys

class tweetReader:

    def __init__(self, filename):
        self.GPS = []
        self.duplicates = 0
        self.tweets = 0
        self.GPStweets = 0
        self.problems = 0
        self.f = open(filename, 'r')
        self.rexLatLon = re.compile(r'(?P<lat>[-]*[0-9]+\.[0-9]+)[^0-9-]+(?P<lon>[-]*[0-9]+\.[0-9]+)')
        
    def getNextTweet(self):
        tweet = Tweet()
        line = self.f.readline()
        if line == "":
        #    print "Missing line:" 
            print (self.tweets,file=sys.stderr) 
            self.f.close()
            return None
        try:
            o = json.loads(line)
            #print o['doc']
            #o = json.loads(o['doc'])
        except json.decoder.JSONDecodeError as e:
            print ("Problematic JSON string:",file=sys.stderr)
            print (line,file=sys.stderr)
            print (e.args,file=sys.stderr)
            self.problems += 1
            return None

       
        # Extract GPS: try 'geo' tag, fallback to 'location' tag
        try:
            if o['doc']['geo'] != None:
                (tweet.lat, tweet.lon) = o['doc']['geo']['coordinates']
                self.GPStweets += 1
            else:
                try:
                    tweet.location = o['doc']['location']
                    match = self.rexLatLon.search(tweet.location)
                    if bool(match):
                        self.GPStweets += 1
                        (tweet.lat, tweet.lon) = float(match.group('lat')), float(match.group('lon'))
                except KeyError:
                    print ("Location Key Error", file=sys.stderr)
                    pass
                #raise
            self.tweets += 1
            if self.tweets%100000 == 0:
                print ("Tweets so far: " + str(self.tweets), file=sys.stderr)

            #Tweet.WRONGuserID = o['from_user_id']
            tweet.userName = o['doc']['from_user']
            if o['doc']['to_user_id'] != None:
                tweet.toUser = o['doc']['to_user']
            else:
                tweet.toUser = None
            tweet.text = o['doc']['text'].encode("utf-8")
            tweet.health = o['doc']['health']
            tweet.createdAt = o['doc']['created_at']
            tweet.profile_image = o['doc']['profile_image_url']
            tweet.msgID = int(o['doc']['id'])
            #print("333333333")
            #tweet.sentiment = float(o['doc']['sentiment'])
            #commenting negemo posemo (PAVAN)
            #tweet.negemo = float(o['doc']['negemo'])
            # tweet.sad = float(o['doc']['sad'])
            #tweet.posemo = float(o['doc']['posemo'])
            #tweet.anger = float(o['doc']['anger'])
            #tweet.friends = float(o['doc']['friends'])
            #print("44444444444")
            tweet.datetime = datetime.strptime(tweet.createdAt, "%a, %d %b %Y %H:%M:%S +0000") - timedelta(hours=4)
            return (tweet, line)
        except KeyError:
            print ("KeyError:",file=sys.stderr)
            print (line, file=sys.stderr)# o
            print ("TWEETS",file=sys.stderr)
            print (self.tweets,file=sys.stderr)
            return ("Err")
  
        
    def printInfo(self):
        print ("_________________________________________________",file=sys.stderr)
        print ("Tweets: %d" % self.tweets, file=sys.stderr)
        print ("Problematic JSON strings: %d" % self.problems, file=sys.stderr)
        print ("GPS locations: %d (rate: %.2f%%)" % (self.GPStweets, self.GPStweets/float(self.tweets)*100 ), file=sys.stderr)


    def getGPSlist(self):
        return self.GPS

