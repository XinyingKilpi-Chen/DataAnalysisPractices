#!/usr/bin/env python3

import math
import numpy as np

def solve_quadratic(a, b, c):
    delta=b**2-4*a*c
    if delta>=0:
        xSmall=(-b-math.sqrt(delta))/(2*a)
        xBig=(-b+math.sqrt(delta))/(2*a)
    else:
        print("There is no sulotion for this quadratic function.")
    return (xSmall,xBig)



def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))

if __name__ == "__main__":
    main()
