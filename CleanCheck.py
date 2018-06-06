"""
Created on Wed Jun  6 11:44:51 2018
Christopher Hall, Wellcome Sanger Institute
@author: ch15@sanger.ac.uk
"""

import os
outfile = open('clean.txt', 'a')
for filename in os.listdir():
    if filename.endswith(".log"):
        with open(filename, 'r', encoding="utf8") as infile:
            for line in infile:
                if ('Bleach' in line or 'DI' in line or 'ShutDownCommand' in line) and 'MeasurementController' not in line:
                    outfile.write(line)
outfile.close()
