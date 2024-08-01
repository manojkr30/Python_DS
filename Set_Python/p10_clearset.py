"""
@Author: Manoj KR

@Date: 2024-07-29 16:38:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-29 16:43:13

@Title : Program to clear set.

"""

def clear_set(numbers):

    """

    description:
        This function is used clear an set.
    
    parameters:
        numbers : set that is going to clear.
        
    return:
        none

    """
    numbers.clear()
    print(numbers)
          

def main():
    numbers = {1, 2, 3, 4, 5}
    clear_set(numbers)


if __name__ == "__main__":
    main()