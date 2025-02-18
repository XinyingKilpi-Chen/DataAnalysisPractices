#!/usr/bin/env python3

def transform(s1, s2):
    '''rst=zip(map(int, string1.split()), map(int, string2.split()))
    list(map(lambda x_y: x_y[0] * x_y[1], rst))'''
    s1Lst = s1.split()
    s2Lst = s2.split()
    s1Int = list(map(int,s1Lst))
    s2Int = list(map(int,s2Lst))
    zipS1S2 = zip(s1Int,s2Int)
    rst = map(lambda x: x[0]*x[1], zipS1S2)
    r=list(rst)
    return r
    #return list(lambda s1Int, sI2nt: {x*y for x,y in zip(s1Int, sI2nt)}, s1Int,s2Int)




def main():
    s1 = "1 5 3"
    s2 = "2 6 -1"
    rst = transform(s1, s2)
    print(list(rst))

if __name__ == "__main__":
    main()
