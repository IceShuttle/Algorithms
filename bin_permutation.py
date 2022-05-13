#!/usr/bin/env python3
import numpy as np

poss = []

def printTheArray(arr, n):
    for i in range(0, n):
        poss.append(arr[i])
 
# Function to generate all binary strings
def generateAllBinaryStrings(n, arr, i):
 
    if i == n:
        printTheArray(arr, n)
        return
     
    # First assign "0" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)
 
    # And then assign "1" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)      



def get_bin_permutations(num):
    generateAllBinaryStrings(num,[None]*num,0)
    possibilites = np.array(poss)
    posssibilites = possibilites.reshape(int(len(poss)/num),num)
    return posssibilites

if __name__=="__main__":
    num = int(input("Enter binary size"))
    print(get_bin_permutations(num))


