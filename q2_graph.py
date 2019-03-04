import math
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches
import time

list1 = []
list2 = []
a = np.arange(100,10000,1)

def time1(n):
    start1 = time.time()
    y = F2(n)
    end1 = time.time()
    temp1 = end1-start1
    list1.append(temp1)

    start2 = time.time()
    z = F3(n)
    end2 = time.time()
    temp2 = end2-start2
    list2.append(temp2)



def F2(n):
    if(n <= 2 ):
        return 1
    else:
        p = 1
        q = 1
        r = 0
        for i in range (3,n+1):
            r = p + q
            p = q
            q = r
        return r

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


for i in a:
    time1(i)


plt.plot(a,list1, label="O(n)", color = 'red')
plt.plot(a,list2, label="O(log(n))", color = 'black' )
# plt.ylim(0,0.0020)
# plt.xlim(0,4000)
plt.xlabel('n')
plt.ylabel('Running time')
plt.title('Running time of F2(n) vs F3(n)')
plt.legend()
plt.show()
