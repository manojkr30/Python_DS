'''
@Author: Manoj KR

@Date: 2024-07-27 16:32:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-27 16:40:15

@Title : To concatenate all elements in a list into a string.
'''
def list_to_string(list):
    """
    Description :To concatenate all elements in a list into a string.

    Parameter : 
              list : list to convert string formate.
     
    Return : 
            string : return the string formate of list.
    """
    string=""
    for i in list:
        string+=str(i)
    return string

if __name__=="__main__":
    list=[4,5,32,65,45,9]
    print(list_to_string(list))