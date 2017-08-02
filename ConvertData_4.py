"""
Input: Tương ứng với mỗi file âm thanh sẽ có 1 thư mục chứa các file tổng mỗi 200 tần số
Output: 80 File .csv dùng để phân lớp. 
"""
import sys

path_in = "./Only 200/"
path_out = "./Only 80/"
for i in range(0, 16):
    for j in range(200, 16001, 200):
        path_file_in = path_in + (str)(i) +"/" + (str)(i) + "_"+ (str)(j) + ".csv"
        print(path_file_in)
        data_file_in = open(path_file_in, 'r')
        line = data_file_in.readline()

        path_file_out = path_out + (str)(j) + ".csv"
        file_open = open(path_file_out,"a")
        file_open.writelines(line)
        file_open.close()
        data_file_in.close()