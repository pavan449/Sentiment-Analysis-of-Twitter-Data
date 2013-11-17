import sys
import simplejson


def writeFile(argfile1, argfile2):
	resfile = open(argfile1,"r")
	predfile = open(argfile2, "r")
	outfile = open("statfile_t.dat", "w")

	outfile.write("from_user\tdate\ttnegamo\tposemo\tsentimentval\tcalcsentiment\n")

	while True:

            head=resfile.readline()

            if not head: 
                break 
	    try:
		
                tweet = simplejson.loads(head)	

		if 'doc' in tweet:
		    doc=tweet["doc"]
		    sentiment = doc["sentiment"]
		    created_at = doc["created_at"]
		    created_at = created_at[:-6]
		    from_user = doc["from_user"]
		
		if 'negemo' in tweet:
	            negemo = tweet["negemo"]
		if 'posemo' in tweet:
		    posemo = tweet["posemo"]
		
		emotionval = predfile.readline()

		if not emotionval:
		    break;

		outfile.write(from_user+"\t"+created_at+"\t"+str(negemo)+"\t"+str(posemo)+"\t"+str(sentiment)+"\t"+str(emotionval));

		from_user=created_at=negemo=posemo=sentiment=emotionval=""	
         

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
