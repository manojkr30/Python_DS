"""
@Author: Manoj KR

@Date: 2024-07-30 11:01:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 11:15:11

@Title : Program to clone a tuple.

"""

def clone_tuple(tuple_of_numbers):

    """

    description:
        This function is used to clone tuple.
    
    parameters:
        tuple_of_numbers(tuple)) : numbers in tuple we are printing.
        
    return:
        none

    """

    cloned_tuple = tuple_of_numbers
    print(cloned_tuple)
    print(id(cloned_tuple))
    print(id(tuple_of_numbers))

def main():
    tuple_of_numbers = (1, 2, 3, 4, (1,3))
    clone_tuple(tuple_of_numbers)
    


if __name__ == "__main__":
    main()