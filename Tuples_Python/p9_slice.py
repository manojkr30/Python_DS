"""
@Author: Manoj KR

@Date: 2024-07-30 12:58:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 13:11:09

@Title : Program to slice a tuple.

"""

def create_tuple(tuple_of_items):

    """

    description:
        This function is used to slice a tuple.
    
    parameters:
        tuple_of_items(tuple) : items in tuple we are slicing in tuple.
        
    return:
        none

    """
    starting_index = int(input("enter starting index postion: "))
    ending_index = int(input("enter ending index postion: "))
    updation = int(input("enter updation value: "))
    print(tuple_of_items[starting_index:ending_index:updation])

def main():
    tuple_of_items = (1, "tarun", (1, 2), 4, [1,3], {'tarun', (1,2)}, {'tarun': 21})
    create_tuple(tuple_of_items)


if __name__ == "__main__":
    main()