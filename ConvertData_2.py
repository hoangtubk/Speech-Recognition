"""
Input: Lấy từ file sau khi chuẩn hóa
Output: Tính theo công thức tọa độ góc để ra các file chứa từng tọa độ X,Y,Z
"""
import numpy as np
from scipy.spatial.distance import euclidean

# from fastdtw import fastdtw
from numpy import genfromtxt
import math

my_data = genfromtxt('Result_10.csv', delimiter=',')
heSo = 1

for hang_ID in range(len(my_data[:,1])):
    sumX = 0
    sumY = 0
    sumZ = 0
    # Chay theo so hang
    data = my_data[hang_ID,:]
    ListToaDo = np.zeros(shape=(len(data),3))
    print("Processing Hang :" + str(hang_ID))
    with open ("./CT_XYZ/" + str(hang_ID) + ".csv", "a") as fileObject:
        for tan_so in range(len(data)):
            """
            if((tan_so >= 25) & (tan_so < 50)):
                heSo = 3
            else:
                if((tan_so >= 50) & (tan_so < 100)):
                    heSo = 2.5
                else:
                    if((tan_so >= 100) & (tan_so < 200)):
                        heSo = 2
                    else:
                        if((tan_so >= 200) & (tan_so < 400)):
                            heSo = 1.5
                        else:
                            if((tan_so >= 400) & (tan_so < 800)):
                                heSo = 1.3
                            else:
                                if((tan_so >= 800) & (tan_so < 1000)):
                                    heSo = 1.2
                                else:
                                    heSo = 1
            """                        
            #print(heSo)
            nang_luong = data[tan_so]
            m = (int)(tan_so/127)
            if((int)(m/2) == 0):
                anpha = 0.7 * (int)((tan_so - m * 127)%128)
            else:
                anpha = 0.7 * (127 - (int)((tan_so-1)%127))
                
            beta = 0.7 * ((int)((tan_so - 1)/127) +1)
            anpha_rad = math.radians(anpha)
            beta_rad = math.radians(beta)
            """
            anpha = heSo * 1.15 * int(tan_so/78)
            anpha_rad = math.radians(anpha)
            beta = heSo * 1.15 * int(tan_so%78)
            beta_rad = math.radians(beta)
            """
            #gamma = 0.015*(tan_so + 1) #Tan so bat dau tu 1
            #gamma_rad = math.radians(gamma)
            x = nang_luong * math.sin(anpha_rad)
            y = nang_luong * math.cos(anpha_rad) * math.sin(beta_rad)
            z = nang_luong * math.cos(anpha_rad) * math.cos(beta_rad)
            sumX += x
            sumY += y
            sumZ += z
            #x = tan_so + 1
            #y = nang_luong * math.sin(gamma_rad)
            #z = nang_luong * math.cos(gamma_rad)
            fileObject.write(str(x) + "," + str(y) + "," + str(z) + "\n")
        
        aph = (180/math.pi)*math.asin(sumZ/(math.sqrt(sumX*sumX+sumY*sumY+sumZ*sumZ)))
        bta = (180/math.pi)*math.asin(sumY/(math.sqrt(sumX*sumX+sumY*sumY)))
        X = 100*math.sin(math.radians(aph))
        Y = 100*math.cos(math.radians(aph))*math.sin(math.radians(bta))
        Z = 100*math.cos(math.radians(aph))*math.cos(math.radians(aph))
        print(aph)
        print(math.radians(aph))
        fileObject.write(str(sumX) + "," + str(sumY) + "," + str(sumZ) + "," + str(aph) + "," + str(bta) + "\n")
        fileObject.write(str(X) + "," + str(Y) + "," + str(Z))
    fileObject.close()
