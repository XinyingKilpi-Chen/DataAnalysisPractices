#!/usr/bin/env python3
def isPositive(x):
    return x>0
def positive_list(L):

    return list(filter(isPositive,L))

def main():
    print(positive_list([2,-2,0,1,-7]) )
    #should return the list [2,1]

if __name__ == "__main__":
    main()
