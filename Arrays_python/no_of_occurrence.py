'''
@Author: Manoj KR

@Date: 2024-07-25 12:51:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 12:56:18

@Title : program to get the number of occurrences of a specified element in an
         array.
'''
import array

def occurrence_of_value(arr,key):
    """
     Description : to get the number of occurrences of a specified element in an array.

    Parameter : 
              arr : input array having group of numbers.
              key : the value occurrence need to be check.
    Return :
            return number of times it occurred in the array
    """
    return arr.count(key)

if __name__=="__main__":
    arr=array.array('i',[4,5,6,7,8,5,9,52,5])
    key=int(input("Enter the value need to finf occurrence in the array :"))
    print(occurrence_of_value(arr,key))