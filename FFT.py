from python_speech_features import fbank

import scipy.io.wavfile as wav
import numpy as np
import sys
import os

def get_list_path_wav(dir):
    """Đọc đường dẫn tất cả file wav trong thư mục dir"""
    list_path = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".wav"):
                list_path.append(os.path.join(root, file))

    return list_path
def get_energy(path_file, path_out):
    name = os.path.basename(path_file)
    file_out = path_out + "/" + name  + ".txt"
    (rate1,sig1) = wav.read(path_file)
    winsize1 = sig1.size*1.0/rate1
    print(winsize1)
    print(sig1.size)
    #mfcc_feat1 = mfcc(sig1,rate1,winsize1,winsize1,16000,16000,sig1.size)
    feat1,energy1 = fbank(sig1,rate1,winsize1,winsize1,16000,16000)#4000,sig1.size,0,4000
    print(energy1)
    print(feat1.size)
    with open(file_out, "w+") as fileObject:
        for x in range(feat1.size):
            fileObject.write(str(feat1[0][x]) + ",")
    fileObject.close()

if __name__ == "__main__":
    path = (str)(sys.argv[1])
    path_out = (str)(sys.argv[2])
    if(path == ""):
        path = "./GhiAm/"
        path_out = "./FFT/"
    
    list_paths = get_list_path_wav(path)
    for one_path in list_paths:
        get_energy(one_path, path_out)