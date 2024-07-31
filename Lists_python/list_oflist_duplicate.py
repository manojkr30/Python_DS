''''
@Author: Manoj KR

@Date: 2024-07-29 15:40:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 16:05:12

@Titl:Python program to remove duplicates from a list of lists.
'''
def remove_duplicate_in_list_of_list(list):
    '''
    Description : to remove duplicates from a list of lists.
   
    Parameter : 
             list : list having list items in it that is list of list.
    Return : 
            return list without duplicate values.
    '''
    result_list=[list[0]]
    for i in range(1,len(list)):
        if list[i] not in result_list:
            result_list.append(list[i])
    return result_list
  
if __name__=='__main__':
    list=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    print(remove_duplicate_in_list_of_list(list))
    