'''
@Author: Manoj KR

@Date: 2024-07-25 16:11:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 16:27:18

@Titl: Program to print all unique values in a dictionary.
'''

def print_unique(dict):
    ''''
    Description : to give all unique values in a dictionary.

    Parameter : 
              dict : dictionary having some duplicate values.
    Return : 
            list : which return all the unique values in the given dictionary.
    '''
    unique_set=set()
    list=dict.values()
    for ele in list:
        unique_set.add(ele)
    return unique_set
        
if __name__=='__main__':
    dict ={1:5,5:89,5:89,4:9,5:8,101:5}
    print(print_unique(dict))