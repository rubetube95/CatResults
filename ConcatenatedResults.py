#quick script for concatenating all files in a folder. This will pull the files name and it's content into a CSV file. 
# SAVE THIS FILE INTO FOLDER WHERE DATA RESIDES. THEN CHANGE *.data TO MATCH FILETYPE *.csv or *.txt AND RUN.

import os
import glob

want_header = True #headers is the original filename. E.g. test.txt, test2.txt, etc.
out_filename = "concatResults.csv"

if os.path.exists(out_filename):
    os.remove(out_filename)

read_files = glob.glob("*.data") #may have to use exact filetype e.g. *.data-nonbm

with open(out_filename, "w") as outfile:
    for filename in read_files:
        with open(filename) as infile:
            if want_header:
                outfile.write('{},Filename\n'.format(next(infile).strip()))
                want_header = False
            else:
                next(infile)
            for line in infile:
                outfile.write('{},{}\n'.format(line.strip(), filename))