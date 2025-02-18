#!/usr/bin/env python3

def interleave(*lists):
    listLen=len(lists)
    zipList=list(zip(*lists))#[(),(),()]
    finalList=[]
    for tupleList in zipList:
        tupleToList=list(tupleList)
        finalList.extend(tupleToList)
    
    #for i in range(listLen):

    
    return finalList

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))


if __name__ == "__main__":
    main()
