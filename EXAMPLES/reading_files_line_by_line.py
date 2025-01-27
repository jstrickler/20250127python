FILE_PATH = '../DATA/mary.txt'

mary_in = open(FILE_PATH)  # open file for reading
# read file...
mary_in.close()  # close file (easy to forget to do this!)

with open(FILE_PATH) as mary_in:  # open file for reading
    # iterate over lines in file (line retains \n)
    for raw_line in mary_in:
        # rstrip() removes whitespace (including \n or \r ) 
        # from end of string
        line = raw_line.rstrip()
        print(line)

