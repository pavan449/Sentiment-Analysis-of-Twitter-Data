import sys
import simplejson

# creates tab separated file containing the sentiment values generated from SVMlight and Sentiment values from LIWC
#usage python StatDatagen_t.py test_tweets_json  prediction_file (out of svm_classifier)

def writeFile(argfile1, argfile2):
	resfile = open(argfile1,"r")
	predfile = open(argfile2, "r")
	outfile = open("statfile_t_sqrt.dat", "w")

	outfile.write("from_user\ttnegamo\tposemo\tsentimentval\tcalcsentiment\tsad\tanger\n")

	while True:

            head=resfile.readline()

            if not head: 
                break 
	    try:
		
                tweet = simplejson.loads(head)	

		if 'doc' in tweet:
		    doc=tweet["doc"]
		    sentiment = doc["sentiment"]
		    from_user = doc["from_user"]
		
		if 'negemo' in tweet:
	            negemo = tweet["negemo"]
		if 'posemo' in tweet:
		    posemo = tweet["posemo"]
		if 'sad' in  tweet:
		    sad = tweet["sad"]
		if 'anger' in tweet:
		    anger = tweet["anger"]
		
		emotionval = (predfile.readline()).rstrip('\n')
		#emotionVal.rstrip('\n')

		if not emotionval:
		    break;

		outfile.write(from_user+"\t"+str(negemo)+"\t"+str(posemo)+"\t"+str(sentiment)+"\t"+str(emotionval)+"\t"+str(sad)+"\t"+str(anger));
		outfile.write("\n")

		from_user=created_at=negemo=posemo=sentiment=emotionval=sad=anger=""	
         

            except ValueError:
                pass
		print "Error Occured"

	resfile.close()
	predfile.close()
	outfile.close()	

def main():
	writeFile(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()	
