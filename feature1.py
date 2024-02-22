import os, time
import numpy as np
import math as mt

def reader():

    flag  = False
    n = 0
    while (flag == False):
        n = input("Unsite broj: ")
        try:
            n = int(n)
            if (n == 0):
                continue
            flag = True
        except:
            pass
            
    sum = n
    while(flag == True):
        inp = input("Unesite broj: ")
        try:
            inp = int(inp)
            if (inp != n):
                break
            sum += inp
        except:
            flag = False
            pass

    return sum

def main():
    sum = reader()
    print(sum)

    return 0

main()

#some additions to the features
#changes to the feature 2