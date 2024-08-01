"""
@Author: Manoj KR

@Date: 2024-07-30 11:38:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 11:45:19

@Title : Program to print repeated elements a tuple.

"""

def repeated_items_tuple(tuple_of_numbers):

    """

    description:
        This function print repeated elements a tuple.
    
    parameters:
        tuple_of_numbers(tuple)) : tuple we are unpacking.
        
    return:
          tuple of repeated elements in given tuple.

    """

    set_repetednumbers = set()
    for i in tuple_of_numbers:
        if tuple_of_numbers.count(i) > 1 :
            set_repetednumbers.add(i)
    return tuple(set_repetednumbers)
            
def main():
    tuple_of_numbers = (1, 1, 2, 3, 4,4)
    print(repeated_items_tuple(tuple_of_numbers))
    

if __name__ == "__main__":
    main()