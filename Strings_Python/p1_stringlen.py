"""
@Author: Manoj KR

@Date: 2024-07-30 13:38:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 13:45:10

@Title : Program to calculate the length of a string.

"""


def length_of_string(string):

    """

    description:
        This function is used to calculate the length of a string.
    
    parameters:
        string(str) : string that going to count length.
        
    return:
        none

    """

    length = 0
    for i in string:
        length += 1
    print(length, "is the length of input string") 

def main():

    string = input("enter a string: ")
    length_of_string(string)


if __name__ == "__main__":
    main()