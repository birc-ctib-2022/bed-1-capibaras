import os
import filecmp

input_test_file_path = "data/input.bed" ## file to parse 
expected_bed_file_path = "data/expected-bedfile.bed" ## manually generated file, what we should expect from 

## file to compare to the expected
outfile_test_path = "data/test_file.bed"

def test_format_bed():
    ## we want to know if the output generated with format_bed is tab separated
    assert filecmp.cmp(outfile_test_path,expected_bed_file_path)

if __name__ == '__main__':
    #execute the program to generate the test bed file
    os.system("python src/format_bed.py " + input_test_file_path + " " + outfile_test_path)
    #format_bed.main()