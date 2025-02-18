#!/usr/bin/env python3
import string
from functools import reduce
def sum_equation(L):
    if not L:
        return "0 = 0"
    else:
        #sum_equation([1,5,7]) returns "1 + 5 + 7 = 13"
        sumL = reduce(lambda x , y: x+y,L,0)
        LStr = list(map(lambda x: str(x), L))
        rst = " + ".join(LStr)+str(f" = {sumL}")
        #append(f" = {sumL}")
        return rst

def main():
    s = sum_equation([])
    print(s)

if __name__ == "__main__":
    main()
