'''
@Author: Manoj KR

@Date: 2024-07-29 14:38:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-29 14:45:19

@Title : Program to add numbers to the sets.

'''

def add_set(numbers):

    """

    description:
        This function is used to add numbers sets.
    
    parameters:
        numbers(set) : numbers in set that are used for iteration and adding to set.
        
    return:
        none

    """
    elements = set()

    for i in numbers:
        elements.add(i)

    print(elements)       

def main():
    numbers = [1, 2, 3, 4, 5]
    add_set(numbers)


if __name__ == "__main__":
    main()