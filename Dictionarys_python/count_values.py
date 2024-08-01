''''
@Author: Manoj KR

@Date: 2024-07-25 16:45:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 16:52:11

@Titl: program to count the values associated with key in a dictionary.
'''
def count_values(dict):
    ''''
    Description : to count the values associated with key in a dictionary.

    Parameter : 
              dict : to count the values in it . 
    Return : 
            sum : integer value the sum of the values in dictionary.
    '''
    sum=0
    for key in dict.keys():
        sum +=dict[key]
    return sum

if __name__=='__main__':
    dict={'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
    print("sum of values =",count_values(dict))

