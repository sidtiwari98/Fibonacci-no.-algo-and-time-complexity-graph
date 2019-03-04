import math
import numpy as np
import matplotlib.pyplot as plt 
import time

list_time = []
a = np.arange(1,30,1)

def time1(n):
    start = time.time()
    y = F1(n)
    end = time.time()
    temp = end-start
    list_time.append(temp)


def F1(n):
    if (n <= 2):
        return 1
    else:
        return (F1(n-1) + F1(n-2))

for i in a:
    time1(i)

plt.plot(a,list_time)
plt.xlabel('n')
plt.ylabel('Running time')
plt.title('Running time of F1(n)')
plt.show()

