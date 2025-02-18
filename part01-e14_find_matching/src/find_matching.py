#!/usr/bin/env python3

def find_matching(L, pattern):
    '''find_matching(["sensitive", "engine", "rubbish", "comment"], "en") should return the list [0, 1, 3]'''
    indexList=[]
    for index, value in enumerate(L):
        if pattern in value:
            indexList.append(index)
    return indexList

def main():
    #list=find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    pass

if __name__ == "__main__":
    main()
