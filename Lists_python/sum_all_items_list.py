''''
@Author: Manoj KR

@Date: 2024-07-29 10:55:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 11:04:11

@Titl: Python program to sum all the items in a list.
'''
def sum_of_list(list_items):
    ''''
    Description : to sum all the items in a given list.

    Parameter : 
              list_items : list having items need to sum all the values.
    Return : 
            sum : sum of all items in given list.
    '''
    sum=0
    for item in list_items:
        sum +=item
    return sum

def main():
    list_items=[45,89,52,100,99,96,58]
    print("sum of all the items in list =", sum_of_list(list_items))
 
if __name__=="__main__":
    main()