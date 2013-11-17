import sys
import simplejson


def getEmoticonsTweets(argfile):
	fil = open(argfile,"r")
	predictfile = open("prediction", "r")
	outfile = open(argfile+".result", "w")

	while True:

            head=fil.readline()
            if not head: 
                break 
	
	    predhead = predictfile.readline()
	    if not predhead:
	        break

	    try:
                tweet = simplejson.loads(head)	
	        if float(predhead) > 0: 
		    tweet['calc_sentiment'] = 1
                else:
                    tweet['calc_sentiment'] = -1

    		simplejson.dump(tweet, outfile)	
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
