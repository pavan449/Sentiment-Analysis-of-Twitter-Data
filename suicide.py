import sys
import simplejson

def getSuicideTweets(argfile):
	fil = open(argfile,"r")
	outfile = open("nyc.trim.suicide", "w")
	all_lines = fil.readlines()
	
	for line in all_lines:
		try:
			tweet = simplejson.loads(line)
			if 'doc' in tweet:
				doc = tweet["doc"]
				text_=doc["text"]
				if "suicid" in text_:
					#print text_
					simplejson.dump(tweet,outfile)
					outfile.write("\n")
		except ValueError:
			pass
			print "Error Occured"
	fil.close()
	outfile.close()	

def main():
	getSuicideTweets(sys.argv[1])

if __name__ == '__main__':
    main()	
