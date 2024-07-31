''''
@Author: Manoj KR

@Date: 2024-07-29 11:12:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 11:20:11

@Titl: Python program to get the smallest number from a list.
'''
def samllest_in_list(list_items):
    ''''
    Description : to get the smallest number from a list.

    Parameter : 
              list_items : list having items need to find the smallest number in it.
    Return : 
            small : the smallest number in the given list.
    '''
    small=list_items[0]
    for item in list_items:
        if item < small:
            small=item
    return small


def main():
    list_items=[45,89,52,100,99,96,58]
    print("The smallest number in given list =", samllest_in_list(list_items))
 
if __name__=="__main__":
    main()