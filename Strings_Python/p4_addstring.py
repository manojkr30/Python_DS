"""
@Author: Manoj KR

@Date: 2024-07-30 14:00:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 14:10:11

@Title :program to add 'ing' at the end of a given string.

"""



def modify_string(string):

    """

    description:
        This function program to add 'ing' at the end of a given string.

    parameters:
        string(str) : string going to add ing at end.
        
    return:
        none

    """

    if len(string) > 3:
        modified_str = string + 'ing'
    else:
        modified_str = string + 'ly'

    print(modified_str)

    
def main():

    global string
    string = input("enter a string: ")
    modify_string(string)

if __name__ == "__main__":
    main()