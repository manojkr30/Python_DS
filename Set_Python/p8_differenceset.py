"""
@Author: Manoj KR

@Date: 2024-07-29 16:30:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-29 16:40:11

@Title : Program to create an difference of set.

"""

def difference_set(numbers1, numbers2):

    """

    description:
        This function is used create an difference of set.
    
    parameters:
        numbers1, numbers2(set) : sets that are going to print difference elements.
        
    return:
        none

    """
    print(numbers1.difference(numbers2))
    print(numbers2.difference(numbers1))
    print(numbers1)
          

def main():

    global numbers1, numbers2 
    numbers1 = {1, 2, 3, 4, 5}
    numbers2 = {2, 3, 4}
    difference_set(numbers1, numbers2)


if __name__ == "__main__":
    main()