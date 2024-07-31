'''
@Author: Manoj KR

@Date: 2024-07-25 12:32:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 12:46:18

@Title : program to to reverse the order of the items in the array.
'''
import array

def reverse_array(arr):
    """
    Description : to to reverse the order of the items in the given array.

    Parameter : 
              arr : input array need to reverse.
     
    Return :
            reverse_array ": the reversed array of user given array.
    """
    reverse_array=array.array('i',[])
    for ele in range(len(arr)-1,0,-1):
        reverse_array.append(ele)
    return reverse_array

def main():
    array_int=array.array('i',[1,2,3,4,5,6])
    print(reverse_array(array_int))
if __name__=="__main__":
    main()