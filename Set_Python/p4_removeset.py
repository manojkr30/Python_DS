'''
@Author: Manoj KR

@Date: 2024-07-29 15:21:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-29 15:28:11

@Title : Program to remove elements sets.

'''

def remove_set(numbers):

    """

    description:
        This function is used to remove elements sets.
    
    parameters:
        numbers(set) : numbers in set that are used for iteration and adding to set.
        
    return:
        none

    """

    numbers.remove(2)
    numbers.remove(3)
    print(numbers)       

def main():
    numbers = {1, 2, 3, 4, 5}
    remove_set(numbers)


if __name__ == "__main__":
    main()