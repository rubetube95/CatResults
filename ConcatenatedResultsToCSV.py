#quick script for concatenating all files in a folder. This will pull the files name and it's content into a CSV file. 
# SAVE THIS FILE INTO FOLDER WHERE DATA RESIDES. THEN CHANGE *.data TO MATCH FILETYPE *.csv or *.txt AND RUN.
# After running, if data in column has data seperated by spaces within the same column use Excel's Data>Text to Columns > Delimited to seperate into seperate columns
#
import glob
import os

out_filename = "combinedFiles.csv"
if os.path.exists(out_filename):
    os.remove(out_filename)

read_files = glob.glob("*.data-nonbm")#may have to use exact filetype e.g. *.data
with open(out_filename, "w") as outfile:
    for filename in read_files:
        with open(filename) as infile:
            for line in infile:
                outfile.write('{},{}\n'.format(line.strip(), filename))


                
                # one below is broken - deletes one entry from each file - need to fix - one above works
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

                
                
