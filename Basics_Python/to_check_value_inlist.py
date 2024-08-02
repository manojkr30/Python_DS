'''
@Author: Manoj KR

@Date: 2024-07-27 16:32:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-27 16:40:15

@Title : To check whether a specified value is contained in a group of values.

'''
def is_contain(list,key):
    """
    Description : heck whether a specified value is contained in a group of values.
   
     Parameter : 
              list : group of numbers stored in list.
              key  : the value need to search in the list.
    Return : 
           boolean : 
              False ->true -> if its Not contain the value the user searching that is key.
              True -> if its contain the value the user searching that is key.
    """

    for i in list:
        if(i==key):
            return True    
    return False

def main():
    list=[1, 5, 8, 3]
    key= 5
    print(is_contain(list,key))

if __name__=="__main__":
    main()
   