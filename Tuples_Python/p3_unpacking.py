"""
@Author: Manoj KR

@Date: 2024-07-29 17:48:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-29 17:55:11

@Title : Program to unpacking a tuple.

"""

def unpacking_tuple(tuple_of_numbers):

    """

    description:
        This function is used to unpacking a tuple.
    
    parameters:
        tuple_of_numbers(tuple)) : tuple we are unpacking.
        
    return:
        none

    """

    a, b, c ,d= tuple_of_numbers
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)


def main():
    tuple_of_numbers = (1, 2, 3, 4)
    unpacking_tuple(tuple_of_numbers)


if __name__ == "__main__":
    main()