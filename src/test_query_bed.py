import os
import filecmp

def test_query_1():
    ## we want to know if the output generated with format_bed is tab separated
    #execute the program to generate the test bed file
    input_test_file_path = "data/large.bed" ## file to parse 
    expected_bed_file_path = "data/expected-1.txt" ## expected result for the 1st query
    query_1_path = "data/query-1.txt" ## first query
    ## file to compare to the expected
    outfile_test_path = "data/test-generated/test_file_query1.bed"
    os.system("python3 src/query_bed.py " + input_test_file_path + " " + query_1_path +" -o" + outfile_test_path) 
    assert  filecmp.cmp(outfile_test_path,expected_bed_file_path)

def test_query_2():
    ## we want to know if the output generated with format_bed is tab separated
    #execute the program to generate the test bed file
    input_test_file_path = "data/large.bed" ## file to parse 
    expected_bed_file_path = "data/expected-2.txt" ## expected result for the 1st query
    query_1_path = "data/query-1.txt" ## first query
    ## file to compare to the expected
    outfile_test_path = "data/test-generated/test_file_query1.bed"
    os.system("python3 src/query_bed.py " + input_test_file_path + " " + query_1_path +" -o" + outfile_test_path) 
    assert  filecmp.cmp(outfile_test_path,expected_bed_file_path) == False


test_query_1()
test_query_2()