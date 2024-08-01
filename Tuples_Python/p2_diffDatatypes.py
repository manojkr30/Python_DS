"""
@Author: Manoj KR

@Date: 2024-07-29 17:38:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-29 17:45:11

@Title : Program to create a tuple with different data types.

"""

def create_tuple(tuple_of_items):

    """

    description:
        This function is used to create tuple with different data types.
    
    parameters:
        tuple_of_items(tuple) : items in tuple we are printing.
        
    return:
        none

    """

    print(tuple_of_items)

def main():
    tuple_of_items = (1, "tarun", (1, 2), 4, [1,3], {'tarun', (1,2)}, {'tarun': 21})
    create_tuple(tuple_of_items)


if __name__ == "__main__":
    main()