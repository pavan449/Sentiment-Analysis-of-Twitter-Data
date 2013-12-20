import sys

#sorting the single features according to the sentiment values in the reverse order

def SortEntries(argfile):
	outfile = open("statfile_t_sorted.dat", "w")
	d_list = [line.strip() for line in open(argfile)]
	d_list.sort(key = lambda line: line.split("\t")[-1], reverse=True)
	for line in d_list:
		outfile.write(line)
		outfile.write("\n")
	outfile.close();

def main():
        SortEntries(sys.argv[1])

if __name__ == '__main__':
    main()
	
