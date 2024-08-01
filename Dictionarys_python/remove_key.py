'''
@Author: Manoj KR

@Date: 2024-07-25 15:59:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 15:65:18

@Titl: Program to remove a key from a dictionary.
'''

if __name__=='__main__':
    dict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    print(dict)
    key=int(input("Enter the Key you need to remove from dictionary :"))
    dict.pop(key)
    print("dictionary after removed element :",dict)