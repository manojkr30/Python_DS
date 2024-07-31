''''
@Author: Manoj KR

@Date: 2024-07-29 11:55:09

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 12:14:03

@Titl: program to remove duplicates from a list.
'''
def remove_duplicat(list):
    '''
    Description : To  remove duplicates elements in the given list and gives the list which is having unique elements in it.

    Parameter : 
              list : list having duplicate and non-duplicate elements given by the user.
    
    Return : None.
            
    '''
    for item in list:
     while list.count(item) > 1 :
           if list.index(item) !=-1:
              list.pop(list.index(item))

def main():
    list=[4,5,6,7,8,9,4,5]
    remove_duplicat(list)
    print(list)

if __name__=="__main__":
    main()