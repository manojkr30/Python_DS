"""
@Author: Manoj KR

@Date: 2024-07-30 16:15:21

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 16:29:01

@Title : Program to count occurrences of a substring in a string.

"""


def occurance_of_substring(string, substring):

    """

    description:
        This function is used to count occurrences of a substring in a string.
    
    parameters:
        string(str) : string counting he occurance of substring
        
    return:
        none

    """

def count_substring_occurrences(string, substring):
    count = 0
    start = 0
    while True:
        start = string.find(substring, start) # Find occurrence of substring starting from 'start'
        if start == -1:
            break
        count += 1
        start += 1  # Move to the next character after the occurrence
    return count



def main():
    string = input("enter a string: ")
    substring = input("enter a substring: ")
    print(count_substring_occurrences(string, substring))


if __name__ == "__main__":
    main()