''''
@Author: Manoj KR

@Date: 2024-07-29 13:06:09

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 13::39

@Titl: Python program to print a specified list after removing the 0th, 4th and
       5th elements.
'''
def remove_index(list,index_list):
    ''''
    Description : To  removing the 0th, 4th and 5th elements in list.

    Parameter : 
              list : list having items need to remove some specific index elements.
              index_list : the index value need to remove from the given list
    
    Return : None        
    '''
    index_list.sort(reverse=True)
    for index in index_list:
        list.pop(index)


if __name__=="__main__":
    list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    remove_index(list,[0,4,5])
    print(list)


