#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    area = triangle.area(1,1)
    print(area)
    hypotenuse = triangle.hypotenuse(1,1)
    print(hypotenuse)

if __name__ == "__main__":
    main()
