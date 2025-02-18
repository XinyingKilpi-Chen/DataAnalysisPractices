#!/usr/bin/env python3

def main():
    #pass
    for i in range(6):
        i+=1
        for j in range(6):
            j+=1
            if i+j==5:
                print(f"({i},{j})")



if __name__ == "__main__":
    main()
