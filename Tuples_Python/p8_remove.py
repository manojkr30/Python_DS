"""
@Author: Manoj KR

@Date: 2024-07-30 12:48:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 12:57:21

@Title : Program to remove an item a tuple.

"""

def remove_item_from_tuple(tuple_of_items, item):

    """

    description:
        This function is used to remove an item from tuple.
    
    parameters:
        tuple_of_items (tuple), item : items in tuple we are removing an item in tuple.
        
    return:
        none

    """

    list_of_items = list(tuple_of_items)
    list_of_items.remove(item)
    print(tuple(list_of_items))
    

def main():

    tuple_of_items = (1, "tarun", (1, 2), 4, [1,3], {'tarun', (1,2)}, {'tarun': 21})
    item = eval(input("enter an item: "))
    remove_item_from_tuple(tuple_of_items,item)


if __name__ == "__main__":
    main()