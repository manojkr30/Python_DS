''''
@Author: Manoj KR

@Date: 2024-07-29 14:55:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 15:07:11

@Titl:Python program to check whether two lists are circularly identical
'''
def are_circularly_identical(list1, list2):
    '''
    Description : The function checks if list2 is a sublist of concatenated_list. To do this, it converts both lists to strings, ignoring the brackets and commas, and checks for the presence of list2 in concatenated_list.

    Parameter : 
              list 1 : list1 having numbers item.
              list 2 : list having numbers item.
    Return : 
            True : if it is circularly_identical
            Fale : if it is Not circularly_identical 
    '''
    if len(list1) != len(list2):
        return False
    concatenated_list = list1 + list1
    return str(list2)[1:-1] in str(concatenated_list)[1:-1]

def main():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 1, 2]
    result = are_circularly_identical(list1, list2)
    print(result) 

if __name__=="__main__":
    main()
