'''
@Author: Manoj KR

@Date: 2024-07-25 15:05:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 15:12:18

@Title :To sort (ascending and descending) a dictionary by value.
'''
def sort_in_ascending(dictionary):
    """
    Description : To sort ascending  a dictionary by value.

    Parameter : 
              dictinary :the user given un sorted key and values .
     
    Return :
             asc_dictionary : which is in ascending order sorted based on values.
    """
    asc_dictionary=sorted(dictionary.items(),key=lambda x : x[1])
    return asc_dictionary

def sort_in_descending(dictionary):
    """
    Description : To sort descending a dictionary by value.

    Parameter : 
              dictinary :the user given un sorted key and values .
     
    Return :
             des_dictionary : which is in descending order sorted based on values.
    """
    des_dictionary=sorted(dictionary.items(),key=lambda x : x[1],reverse=True)
    return des_dictionary


if __name__=="__main__":
    marks={"manoj":35,
                "ramesh":95,
                "kavitha":90,
                "gagana":85
                }
    print(f"The Marks in Ascending Order :{sort_in_ascending(marks)}")
    print(f"The Marks in Descending Order :{sort_in_descending(marks)}")