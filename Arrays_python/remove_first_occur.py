'''
@Author: Manoj KR

@Date: 2024-07-25 13:00:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 13:09:18

@Title : program to remove the first occurrence of a specified element from an array.
'''
import array

def remove_first_occurrence(arr,key):
    '''
    Description : to to remove the first occurrence of a specified element from an array.
    Parameter : 
              arr : input array having group of numbers.
              key : the value occurrence need to be check and delet first occurrence.
    Return :
            return array which the first occurrence of key gets deleted .

    '''
    for ele in arr:
        if(ele==key):
            arr.remove(key)
            return arr
    return arr


if __name__=="__main__":
    arr=array.array('i',[4,5,6,7,8,5,9,52,5])
    key=int(input("Enter the value need to remove first occurence from the array :"))
    print(remove_first_occurrence(arr,key))