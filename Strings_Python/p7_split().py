"""
@Author: Manoj KR

@Date: 2024-07-30 15:20:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-30 15:29:11

@Title : program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

"""


def arrange_alpha_numarically(string_of_words):

    """

    description:
        This function is used program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
    
    parameters:
        string_of_words(str) : string_of_words that going to count character frequency.
        
    return:
        none

    """

    words = string_of_words.split(',')
    words = [word.strip() for word in words]
    unique_words = set(words)
    unique_words = sorted(unique_words)
    unique_words = ','.join(unique_words)

    print(unique_words)


def main():

    string_of_words = "red, white, black, red, green, black"
    arrange_alpha_numarically(string_of_words)


if __name__ == "__main__":
    main()