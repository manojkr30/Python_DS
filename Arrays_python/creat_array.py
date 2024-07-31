'''
@Author: Manoj KR

@Date: 2024-07-25 16:62:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 17:15:18

@Title : program to create an array of 5 integers and display the array items.
         Access individual element through indexes.
'''

# Importing the array module
import array

if __name__=="__main__":
    int_array = array.array('i', [1, 2, 3, 4, 5])

    print("Accessing individual elements through indexes:")
    for i in range(len(int_array)):
        print(f"Element at index {i}: {int_array[i]}")