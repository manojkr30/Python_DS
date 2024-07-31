''''
@Author: Manoj KR

@Date: 2024-07-29 14:38:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 14::11

@Titl:Python program to append a list to the second list.
'''
def list_append(list1,list2):
    '''
    Description : To append a list to the second list.

    Parameter : 
              list 1 : list1 having numbers item.
              list 2 : list having numbers item.
    Return : returns the list 1 + list 2 append together .    
    '''
    return list1 + list2
  
def main():
    list1=[2,3,4,5,6,8,9]
    list2=[1,2,3,4,5,6]
    print(list_append(list1,list2))

if __name__=="__main__":
    main()