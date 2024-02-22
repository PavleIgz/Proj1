import os, time
import numpy as np
import math as mt

def function():

    flag = False
    number = 0
    while (flag == False):

        s = input("Unesite integer velicinu matrice: ")
        try:
            number = int(s)
            if (number == 0):
                print("Invalid input!")
                continue
            if (number < 0):
                number *= -1
            flag = True
        except:
            print("Invalid input!")
            pass
    
    return number

def main():

    n = function() #n su rows, koliko arrayeva od m članova ima
    m = int(n * 3 / 2)     #m su columns, koliko članova ima u jednom arrayu

    mat = np.array([None] * n * m).reshape(n, m)
    
    i = 0
    j = 0
    for i in range(n):
        for j in range(m):
            if (j <= i):
                mat[i][j] = 111
            else:
                 mat[i][j] = 000

    for i in range(n):
            print(f"{mat[i]} ") #printamo n puta, arrayeve velicine m
    
    

    return 0


main()

#some changes, commit 2
#changes to the feature 2
