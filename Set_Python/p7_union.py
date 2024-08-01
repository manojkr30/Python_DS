"""
@Author: Manoj KR

@Date: 2024-07-29 16:13:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-29 16:25:11

@Title : Program to create an union of set.

"""

def union_set(numbers1, numbers2):

    """

    description:
        This function is used create an union of set.
    
    parameters:
        numbers1, numbers2(set) : sets that are going to print union elements.
        
    return:
        none

    """
    # numbers1.update(numbers2)  
    # print(numbers1.update(numbers2))   
    print(numbers1.union(numbers2))

def main():
    numbers1 = {1, 27, 30, 4, 5}
    numbers2 = {2, 30, 4, 7, 90, 6}
    union_set(numbers1, numbers2)


if __name__ == "__main__":
    main()