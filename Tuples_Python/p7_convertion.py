"""
@Author: Manoj KR

@Date: 2024-07-30 12:08:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 12:15:11

@Title : Program to convert a list into a tuple.

"""

def create_tuple(list_of_numbers):

    """

    description:
        This function is used to convert a list into a tuple.
    
    parameters:
        list_of_numbers(list)) : list that we are converting into tuple.
        
    return:
        none

    """

    print(tuple(list_of_numbers))

def main():
    list_of_numbers = [1, 2, 3, 4]
    create_tuple(list_of_numbers)


if __name__ == "__main__":
    main()