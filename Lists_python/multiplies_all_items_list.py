''''
@Author: Manoj KR

@Date: 2024-07-29 10:06:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 11:11:11

@Titl: Python program to multiplies all the items in a list.
'''
def multiplies_of_list(list_items):
    ''''
    Description : to multiplies all the items in a given list.

    Parameter : 
              list_items : list having items need to multiplies all the values.
    Return : 
            mul : multiplies of all items in given list.
    '''
    mul=1
    for item in list_items:
        mul *=item
    return mul

def main():
    list_items=[4,2,1,9,6,8]
    print("multiplies of all the items in list =", multiplies_of_list(list_items))
 
if __name__=="__main__":
    main()