"""
@Author: Manoj KR

@Date: 2024-07-30 14:01:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 14:13:11

@Title : Program to count the number of characters (character frequency) in a string.

"""


def char_frequency(string):

    """

    description:
        This function is used to count the number of characters (character frequency) in a string.
    
    parameters:
        string(str) : string that going to count character frequency.
        
    return:
        none

    """

    char_frequency = set()
    for i in string:
        if i not in char_frequency:
            char_frequency.add(i+str(string.count(i)))
    list_of_items=[]
    list_of_items=char_frequency
    print("".join(sorted(list_of_items,key=lambda x : x[1],reverse=True)))

def main():

    string = 'google.com'
    char_frequency(string)


if __name__ == "__main__":
    main()