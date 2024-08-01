"""
@Author: Manoj KR

@Date: 2024-07-30 11:48:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 11:59:01

@Title : Program to check whether an element exists within a tuple.

"""

def element_in_tuple(tuple_of_numbers, element):

    """

    description:
        This function to check whether an element exists within a tuple.
    
    parameters:
        tuple_of_numbers(tuple)) : tuple to check the element is exsists.
        
    return:
        none

    """         
    if tuple_of_numbers.count(element) > 0 :
        print(element, "element exists")
    else:
            print(element, "not exists")

    
def main():

    global tuple_of_numbers, element
    element = int(input("enter a number to check : "))
    tuple_of_numbers = (1, 10, 12,101, 3, 4)
    element_in_tuple(tuple_of_numbers, element)


if __name__ == "__main__":
    main()