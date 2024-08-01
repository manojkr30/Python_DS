"""
@Author: Manoj KR

@Date: 2024-07-30 14:20:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 14:29:11

@Title : Program that takes a list of words and returns the length of the longest one.

"""


def long_length_string(list_of_words):

    """

    description:
        This function that takes a list of words and returns the length of the longest one.

    parameters:
        list_of_words(list) : in the list printing the longest length string.
        
    return:
        none

    """

    list_of_lengths = []
    for i in list_of_words:
        list_of_lengths.append(len(i))
    list_of_lengths.sort(reverse = True)
    print(list_of_lengths[0])

    
def main():

    global list_of_words
    list_of_words = eval(input("enter list of words: "))
    long_length_string(list_of_words)

if __name__ == "__main__":
    main()