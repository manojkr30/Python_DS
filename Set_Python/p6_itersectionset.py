"""
@Author: Manoj KR

@Date: 2024-07-29 15:50:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-29 15:59:11

@Title : Program to create an intersection of set.

"""

def itersection_set(numbers1, numbers2):

    """

    description:
        This function is used create an intersection of set.
    
    parameters:
        numbers1, numbers2(set) : sets that are going to print intersection elements.
        
    return:
        none

    """
    numbers = set()
   
    print(numbers1.intersection(numbers2))       

def main():
    numbers1 = {1, 2, 3, 4, 5,9}
    numbers2 = {2, 3, 4,6,8}
    itersection_set(numbers1, numbers2)


if __name__ == "__main__":
    main()