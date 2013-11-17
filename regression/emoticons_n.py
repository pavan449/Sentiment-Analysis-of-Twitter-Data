import sys
import simplejson

emotions = ("<3","(:",":(",":-(",";(","=(",":-/","):")

def getEmoticonsTweets(argfile):
	fil = open(argfile,"r")
	resfile = open(argfile+".res", "w")
	outfile = open(argfile+".negative", "w")
	while True:

            head=fil.readline()
            if not head: 
                break 
	    try:
		
                tweet = simplejson.loads(head)	
	        found = -1
	
		if 'doc' in tweet:
	            doc = tweet["doc"]
		    text_=doc["text"]

	            for el in emotions:
		        index = text_.find(el)
			if (index > 0):
			    simplejson.dump(tweet,outfile)
			    outfile.write("\n")
			    found = 1
			    break

		    if found == -1:	    
		        simplejson.dump(tweet,resfile)
			resfile.write("\n")
	
         

            except ValueError:
                pass
		print "Error Occured"

	fil.close()
	outfile.close()	
	resfile.close()

def main():
	getEmoticonsTweets(sys.argv[1])

if __name__ == '__main__':
    main()	
