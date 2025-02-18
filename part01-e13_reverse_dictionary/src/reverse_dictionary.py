#!/usr/bin/env python3

def reverse_dictionary(d):
    '''d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reverse_dictionary(d)
    {'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}'''
    resultDict={}
    for key, values in d.items():
        for value in values:
            if value in resultDict:
                resultDict[value].append(key)
            else:
                resultDict[value]=[key]
    return resultDict

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reversedD=reverse_dictionary(d)
    print(reversedD)

if __name__ == "__main__":
    main()
