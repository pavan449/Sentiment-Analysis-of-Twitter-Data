import sys
import simplejson

emotions = ("<3","(:",":(",":-(",";(","=(",":/",":-/","):")

def getEmoticonsTweets(argfile):
	fil = open(argfile,"r")
	outfile = open("nyc.trim.emoticons.negative", "w")
	all_lines = fil.readlines()
	
	for line in all_lines:
		try:
			tweet = simplejson.loads(line)
			if 'doc' in tweet:
				doc = tweet["doc"]
				text_=doc["text"]
				for el in emotions:
					index = text_.find(el)
					if (index > 0):
						if(el == ":/"):
							if(text_[index-1] == 'p'):
								continue
						simplejson.dump(tweet,outfile)
						outfile.write("\n")
		except ValueError:
			pass
			print "Error Occured"
	fil.close()
	outfile.close()	

def main():
	getEmoticonsTweets(sys.argv[1])

if __name__ == '__main__':
    main()	
