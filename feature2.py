import os, time
import numpy as np
import math as mt
import sys



def newfunction():

    n = 10
    arr = np.array([None] * n * n).reshape(10, 10)
    for i in range(10):
        for j in range(10):
            if (i >= j):
                arr[i][j] = i + j
            else:
                arr[i][j] = 0
    
    return arr

def main():

    arr = newfunction()
    for i in range(10):
        print(arr[i])

    return 0

main()