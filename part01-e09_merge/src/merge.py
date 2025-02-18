#!/usr/bin/env python3
import numpy as np
def merge(L1, L2):
    L1Len=len(L1)
    L2Len=len(L2)
    i=0
    j=0
    L=[]
    while i <L1Len or j <L2Len:
        
        if i==L1Len:
            L.append(L2[j])
            j+=1
        elif j==L2Len:
            L.append(L1[i])
            i+=1
        elif L1[i]<=L2[j]:
            L.append(L1[i])
            i+=1
        elif i==L1Len and j==L2Len:
            break
        else:
            L.append(L2[j])
            j+=1
    return L

def main():
    L1=[1,3,5,7,9]
    L2=[2,6,8,10]
    L=merge(L1,L2)
    print(L)

if __name__ == "__main__":
    main()
