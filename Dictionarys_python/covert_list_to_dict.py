''''
@Author: Manoj KR

@Date: 2024-07-25 17:45:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 17:59:11

@Titl: program to convert a list into a nested dictionary of keys.
'''
def list_to_nested_dict(lst):
    ''''
    Description : to convert a  given list into a nested dictionary of keys.

    Parameter : 
              list : list need to covert into a nested dictionary of keys.
    Return : 
            nested_dict : which return nested dictionary for given list.
    '''
    nested_dict = current_level = {}
    for key in lst:
        current_level[key] = {}
        current_level = current_level[key]
    return nested_dict

def main():
    my_list = ["a", "b", "c", "d"]
    nested_dict = list_to_nested_dict(my_list)
    print(nested_dict)

if __name__=="__main__":
    main()