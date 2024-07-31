''''
@Author: Manoj KR

@Date: 2024-07-29 15:09:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 15:20:10

@Titl:Python program to find common items from two lists.
'''
def common_items(list1,list2):
    '''
    Description : to find common items from two lists.

    Parameter : 
              list 1 : list1 having numbers item.
              list 2 : list2 having numbers item.
    Return : 
            return list1 items which are in the list2 that are common items. 
    '''
    return [item for item in list1 if item in list2]

def main():
    list1 = [1, 2, 3,8,69,98]
    list2 = [3, 4, 1, 2]
    # result = 
    print(common_items(list1, list2)) 

if __name__=="__main__":
    main()
