from tkinter import Y
import matplotlib.pyplot as plt; 
import numpy as np; 
import random;
plt.rcParams['figure.figsize']= [10,5]
import csv

noofexp = 1000000

def findavg(k):
    s = 0
    for i in range(51):
        s = i*k[i]+s
    return(s/1000000)

def give():
    return(random.random())

def gen():
    x, k = [],[]
    z = 0
    y = [0 for x in range(51)]
    for i in range(noofexp):
        z = give()
        if z<=0.4:
            if len(x)>0:
                x.pop()
        w = give()
        if w<=0.3:
            x.append(5)
        y[len(x)] = y[len(x)]+1
        if (len(x)==0):
            k.append(i)
    z = findavg(y)
    for j in range(51):
        y[j]=y[j]/noofexp
    #return(y, k[len(k)-1])
    return(y,z)

y1, k = gen()
x1 = [x for x in range(51)]

print('Time average of number of packets in the memory:', k)
plt.stem(x1, y1, use_line_collection = True)
plt.show()

