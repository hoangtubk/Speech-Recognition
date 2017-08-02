"""
Input: từ mỗi file tọa độ X, Y, Z
Output: Tính tổng năng lượng và ghi ra file mỗi 200 năng lượng một file 
"""

import sys

def Function(STT):
    FileData = "./CT_XYZ/" + STT + ".csv" 
    hFileData = open(FileData, 'r')
    loop_line = 0
    tongX = 0
    tongY = 0
    tongZ = 0
    for loop in range(1, 16001):
        line = hFileData.readline()
        data = line.split(",")
        tongX = tongX + (float)(data[0])
        tongY = tongY + (float)(data[1])
        tongZ = tongZ + (float)(data[2])
        if (loop%200 == 0):
            FileOut = "./Only 200/" + STT + "/" + STT + "_" + (str)(loop) + ".csv"
            with open (FileOut, "a") as fileObject:
                fileObject.write((str)(tongX) + "," + (str)(tongY) + "," + (str)(tongZ))
                fileObject.write("\n")
            fileObject.close()
            tongX = 0
            tongY = 0
            tongZ = 0
    hFileData.close()

if __name__ == "__main__":
    for STT in range(0, 16):
        Function((str)(STT))