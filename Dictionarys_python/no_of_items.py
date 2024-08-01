''''
@Author: Manoj KR

@Date: 2024-07-25 17:45:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 17:59:11

@Titl: program to count number of items in a dictionary value that is a list.
'''
def count_items_in_list_values(dictionary):
    '''
     Description : to count number of items in a dictionary value that is a list.

    Parameter : 
              dictionary : to count the list element in given dictionary. 
    Return : 
            count : the number of elements of all list in dictionary.
    
    '''
    count = 0
    for value in dictionary.values():
        if isinstance(value, list):
            count += len(value)
    return count

def main():
    sample_dict = {
    'a': [1, 2, 3],
    'b': [4, 5],
    'c': 6,
    'd': [7, 8, 9, 10],
    'e': 'hello'
    }
    result = count_items_in_list_values(sample_dict)
    print(f"Number of items in dictionary values that are lists: {result}")

if __name__=="__main__":
    main()
