''''
@Author: Manoj KR

@Date: 2024-07-29 11:20:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 11:35:11

@Titl:Python program to get the difference between the two lists.
'''
def diffrence_between(list1,list2):
    '''
    Description : To get the difference between the two lists.

    Parameter : 
              list 1 : list having numbers.
              list 2 : list having numbers.
    Return : returns the list 1 items which are not in the list2.        
    '''
    return [item for item in list1 if item not in list2]
def main():
    list1={2,3,4,5,6,8,9}
    list2={1,2,3,4,5,6}
    print(diffrence_between(list1,list2))

if __name__=="__main__":
    main()