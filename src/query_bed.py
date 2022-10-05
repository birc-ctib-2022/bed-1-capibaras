"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    parse_line, print_line
)
from query import Table


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',  # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
        

    #read the file (in this case it's a bed and a query)
    #mytab = Table() #to initialize the table
    #for line in args.bed:
    #    mytab.add_line(parse_line(line)) #add a line to the table
    #print(mytab) 
    #now we have a table with the bedfiles, which is the lines that we want to check if they're in the query

    #now we read the query and 1 --> check whether the chr.query is inside bedfile
    #                           2--> check for the lengths

    bed_file = Table() ## process bed file (input)
    for line in args.bed:
        bed_file.add_line(parse_line(line))

    for line in args.query: ## process the query and check if it exists in the input file
        chrom, start, end = line.split() ## process the line of the query
        coincidences = bed_file.get_chrom(chrom)
        if len(coincidences) > 0:  ## is our chromosome in the bed table? 
            for c in coincidences: ## check the range of each coincidence
                if int(start) <= c[1] and c[2] >= int(end):
                    print_line(c,args.outfile)



if __name__ == '__main__':
    main()
                                            #what the input asks for
#python 3.10 | name of file you want to run | input.bed | input.query | output file