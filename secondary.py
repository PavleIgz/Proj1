import os, time
import numpy as np
import math as mt


def funkcija():
    str = input("Unesite string: ")
    arr = []
    for c in str:
        arr.append(c)
    numbers = []

    for i in range(len(arr)):
        try:
            n = int(arr[i])
            print(f"number: {n}")
            numbers.append(n)
        except:
            pass
    return numbers


def main():
    arr = funkcija()
    print(arr)

    return 0

main()

