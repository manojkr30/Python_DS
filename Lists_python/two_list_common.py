''''
@Author: Manoj KR

@Date: 2024-07-29 12:56:09

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 12:59:39

@Titl: Python function that takes two lists and returns True if they have at
       least one common member.
'''
def is_common_member(list1,list2):
    '''
    Description : function that takes two lists and returns True if they have at
                  least one common member.

    Parameter : 
              list1 ,list2 : two list to find common members between.
    Return : 
            True : if its have at least one common member between 2 list.
            False : if there is No common members between 2 list,
    '''
    for item in list1:
        if list2.count(item) >= 1 :
            return True
    return False

def main():
    list1=[1,2,3,4,5,6]
    list2=[10,9,8,7,6]
    print(is_common_member(list1,list2))

if __name__=="__main__":
    main()
