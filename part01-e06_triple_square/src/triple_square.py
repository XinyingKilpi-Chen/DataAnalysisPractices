#!/usr/bin/env python3
def triple(i):
    return i*3

def square(i):
    return i**2

def main():
    for i in range(1,11):
        #it stops iteration when the square of a value 
        # is larger than the triple of the value
        sq=square(i)
        tp=triple(i)
        if sq<=tp:
            print(f"triple({i})=={tp} square({i})=={sq}")
        else:
            break

if __name__ == "__main__":
    main()
