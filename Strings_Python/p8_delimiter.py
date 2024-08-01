"""
@Author: Manoj KR

@Date: 2024-07-30 15:38:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 15:49:03

@Title : Program to get the last part of a string before a specified character.

"""


def print_last_part(string, delimiter):

    """

    description:
        This function is used program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
    
    parameters:
        string, delimiter(str) : string which needs to be print last of before specific delimiter.
        
    return:
        none

    """


    delimiter_index = string.rfind(delimiter)

    if delimiter_index != -1:
        result = string[:delimiter_index:]

    else:
        result = string

    print(result)

def main():
    
    string = input("enter a string: ")
    delimiter = input("enter a delimiter: ")
    print_last_part(string, delimiter)


if __name__ == "__main__":
    main()