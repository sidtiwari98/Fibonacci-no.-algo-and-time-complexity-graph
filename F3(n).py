#O(log n) 

import numpy as np

def power_of_G(n):
    G = np.array([[0,1], [1,1]])
    if(n == 1):
        return G
    else:
        if( n%2 == 0):
            H = power_of_G(n/2)
            C = np.dot(H , H)
            return C  #returning H X H
        else:
            H = power_of_G((n-1)/2) 
            C = np.dot(H , H)
            temp = np.dot(C , G)
            return temp #returning H x H x G


def F3(n):
    temp = power_of_G(n)
    return temp[0][1]


input = open("input3.txt", "r")
fileRead = input.readlines()
output = open("output3.txt", "w")
 
for x in fileRead:
    num = (F3(int(x)))
    output.write(str(num)+ "\n")