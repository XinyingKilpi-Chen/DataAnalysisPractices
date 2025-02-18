#!/usr/bin/env python3

def detect_ranges(L):
    LSorted=sorted(L)
    print(LSorted)
    s=0
    e=0
    result=[]
    while e<len(LSorted):
        if e==len(LSorted)-1:# e is the last one
            if s==e:
                result.append(LSorted[s])
                break
            else:
                result.append((LSorted[s],LSorted[e]+1))
                break
        else:
            if LSorted[e+1]-LSorted[e]==1:
                e+=1
            elif s==e:#difference is not 1
                result.append(LSorted[s])
                s+=1
                e+=1
            else:#difference is not 1 and more s!=e
                result.append((LSorted[s],LSorted[e]+1))
                e+=1
                s=e

    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
