import sys
import simplejson

#utility file to count the number of Tweets
def getEmoticonsTweets(argfile):
	print argfile
	filedata = open(argfile,"r")
	count = 0
	while True:
	    head = filedata.readline()
	    if not head:
		break
	    count=count+1
		 
	filedata.close()
	print count
def main():
	getEmoticonsTweets(sys.argv[1])

if __name__ == '__main__':
    main()	
