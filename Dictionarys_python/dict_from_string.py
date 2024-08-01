''''
@Author: Manoj KR

@Date: 2024-07-25 16:35:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 16:42:11

@Titl: program to create a dictionary from a string. Note: Track the count of the letters from the string.
'''
def string_t0_dict(string):
    ''''
    Description : to create a dictionary from a string.

    Parameter : 
              string : user given string need to convert dictionary. 
    Return : 
            dict : dictionary that having string and int value the no of times that character occurres in given string.
    '''
    dict={}
    unique_set=set(string)
    for ele in unique_set:
        dict.update({ele : string.count(ele)})
    return dict
if __name__=='__main__':
    string='w3resource'
    print(string_t0_dict(string))