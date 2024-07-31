''''
@Author: Manoj KR

@Date: 2024-07-29 11:40:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 11:51:19

@Titl:Python program to get a list, sorted in increasing order by the last
      element in each tuple from a given list of non-empty tuples.
'''
def sort_list_tuple(list):
    '''
    Description : To  get a list, sorted in increasing order by the last
                  element in each tuple from a given list of non-empty tuples.

    Parameter : 
              list : list having tuples as a items .
    Return : 
            return sorted list.
    '''
    return (sorted(list,key=lambda x : x[-1]))

def main():
    list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_list_tuple)

if __name__=="__main__":
    main()