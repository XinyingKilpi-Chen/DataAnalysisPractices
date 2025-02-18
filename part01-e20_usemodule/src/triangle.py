# Enter you module contents here
'''Module for calculations related to right-angled triangles.
Two functions:
1. hypotenuse: calculate the hypotenuse of a right-angled triangle
2. area: calculate the area of a right-angled triangle

Attributes:
    __version__(str)
    __author__(str)
'''
__version__ = "1.0"
__author__ = "Xinying Kilpi-Chen"
def hypotenuse(s1, s2):
    '''Function to calculate the hypotenuse side of a right-angled triangle
    Arg:
        s1(float): one side
        s2(float): another side
    Returns:
        float: length of the hypotenuse

    '''
    return (s1**2+s2**2)**(1/2)

def area(s1, s2):
    '''Calculate the area of a right-angled triangle
    Args:
        s1(float): one side
        s2(float): another side
    Returns:
        float: area of the right-angled triangle
    '''
    return s1*s2/2