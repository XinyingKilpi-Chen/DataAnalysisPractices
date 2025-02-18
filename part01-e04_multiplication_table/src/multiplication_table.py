#!/usr/bin/env python3


def main():
    #pass
    for i in range(10):
        i+=1
        for j in range(10):
            j+=1
            result=i*j
            print('{:4d}'.format(result),end="")
            '''if j<10:
                print('{:4d}'.format(result),end="")
            else:
                print('{:4d}'.format(result))'''
        print('\n',end="")


if __name__ == "__main__":
    main()
