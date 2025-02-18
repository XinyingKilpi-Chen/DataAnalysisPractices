#!/usr/bin/env python3

def distinct_characters(L):
    '''Use the set container to temporarily store the distinct characters in a string. 
    Example of usage: distinct_characters(["check", "look", "try", "pop"]) 
    should return { "check" : 4, "look" : 3, "try" : 3, "pop" : 2}'''
    resultDict={}
    for item in L:
        resultDict[item]=len(set(item))
    return resultDict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))
    

if __name__ == "__main__":
    main()
