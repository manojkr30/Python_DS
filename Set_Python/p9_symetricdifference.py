"""
@Author: Manoj KR

@Date: 2024-07-29 16:41:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-29 16:55:11

@Title : Program to create an symmetric difference of set.

"""

def symmetric_difference_set(numbers1, numbers2):

    """

    description:
        This function is used create an symmetric difference of set.
    
    parameters:
        numbers1, numbers2(set) : sets that are going to print symmetric difference elements.
        
    return:
        none

    """
    print(numbers1.symmetric_difference(numbers2))
          

def main():
    numbers1 = {1, 2, 3, 4, 5}
    numbers2 = {2, 3, 4, 5.7 ,9}
    symmetric_difference_set(numbers1, numbers2)


if __name__ == "__main__":
    main()