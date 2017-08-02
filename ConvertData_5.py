"""

"""
import sys
import csv

path_input = "Result_10.csv"
path_output = "Matrix_Result_10.csv"
file_in = open(path_input,'r')
file_out = open(path_output,'a')
tong = 0.0
data = csv.reader(file_in)

for row in data:
    for i in range(0, 16000):
        if((i + 1)%200 != 0):
            tong = tong + (float)(row[i])
        else:
            if(tong < 0.01):
                file_out.write("0,")
            else:
                file_out.write("1,")
            tong = 0    
    file_out.write("\n")
file_in.close