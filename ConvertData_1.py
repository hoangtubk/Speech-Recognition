"""
Input: File sau khi đã tính FFT với mỗi tần số, tính giá trị năng lượng max mỗi dòng
OutPut: File chuẩn hóa theo năng lượng max.
"""

import sys
FileData = "ChuaChuanHoa_MAX.csv" 
hFileData = open(FileData, 'r')
loop = 0
with open ("Result_10.csv", "a") as fileObject:
    while 1:
        line = hFileData.readline()
        data = line.split(",")
        loop = 0
        for x in data:
            loop = loop + 1
            print(data[1])
            y =  float( float(x) /float(data[16000]))
            fileObject.write(str(y))
            if loop  != 16000:
                fileObject.write(",")
            else:
                break
        fileObject.write("\n")
fileObject.close()
hFileData.close()
            
