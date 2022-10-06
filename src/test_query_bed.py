import os
import filecmp

input_test_file_path = "data/large.bed" ## file to parse 
expected_bed_file_path = "data/expected-1.txt" ## expected result for the 1st query
query_1_path = "data/query-1.txt" ## first query
## file to compare to the expected
outfile_test_path = "data/test-generated/test_file_query1.bed"

def test_query_1():
    ## we want to know if the output generated with format_bed is tab separated
    assert filecmp.cmp(outfile_test_path,expected_bed_file_path)

test_query_1()

if __name__ == '__main__':
    #execute the program to generate the test bed file
    os.system("python3 src/query_bed.py " + input_test_file_path + " " + query_1_path +" -o" + outfile_test_path)
    #format_bed.main()