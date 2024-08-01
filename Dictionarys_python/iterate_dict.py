'''
@Author: Manoj KR

@Date: 2024-07-25 15:39:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 15:45:18

@Title : program to iterate over dictionaries using for loops.
'''
def iterate(dict):
    ''''
    Description : To to iterate over dictionaries using for loops.

    Parameter : 
              dictinary :the user given dictionary to traverse.
     
    Return : None
    '''
    for ele in dict.keys():
        print(f"{ele}-->{dict[ele]}")

if __name__=='__main__':
    dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    iterate(dict)
   