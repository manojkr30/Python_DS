"""
@Author: Manoj KR

@Date: 2024-07-29 17:28:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-29 17:40:1

@Title : Program to print min and max numbers of set.

"""

def min_max(numbers):

    """

    description:
        This function is used print min and max numbers of set.
    
    parameters:
        numbers : set going to find the min and max numbers.
        
    return:
        none

    """
    list_of_numbers = list(numbers)
    list_of_numbers.sort()
    min_number = list_of_numbers[0]
    max_number = list_of_numbers[-1]
    print(min_number, "is minimum number")
    print(max_number, "is maximum number")
    

def main():

    global numbers 
    numbers = {1, 3, 5, 83, 0}
    min_max(numbers)


if __name__ == "__main__":
    main()