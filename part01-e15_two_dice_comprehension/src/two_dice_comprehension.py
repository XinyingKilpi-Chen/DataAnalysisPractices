#!/usr/bin/env python3

def main():
    '''for i in range(6):
        i+=1
        for j in range(6):
            j+=1
            if i+j==5:
                print(f"({i},{j})")'''
    #s={ i*j for i in range(10) for j in range(10)}
    dicePair={ (i,j) for i in range(1,7) for j in range(1,7) if i+j==5}
    for diceNum in dicePair:
        print(diceNum)

if __name__ == "__main__":
    main()
