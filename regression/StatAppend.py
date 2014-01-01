# Appends the calculated sentimentvalue to json with the new field "calc_sentiment"
# usage: python StatAppend.py test_data_set prediction_File
#
import sys
import simplejson


def writeFile(argfile1, argfile2):
	resfile = open(argfile1,"r")
	predfile = open(argfile2, "r")
	outfile = open(argfile1+".append.sentiment", "w")


	while True:

            head=resfile.readline()

            if not head: 
                break 
	    try:
		
                tweet = simplejson.loads(head)	

		emotionval = (predfile.readline()).rstrip('\n')
		
		if not emotionval:
		    break;

    	  	tweet["calc_sentiment"] = emotionval


		outfile.write(simplejson.dumps(tweet))

		outfile.write("\n")

		emotionval=""	
         

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
