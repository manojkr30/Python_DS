''''
@Author: Manoj KR

@Date: 2024-07-29 15:20:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 15:36:12

@Titl:Python program to split a list based on first character of word.
'''
def split_list_by_first_char(words_list):
    '''
    Description : to split a list based on first character of word.
   
    Parameter : 
             words_list : list having string items in it.
    Return : 
            return list wich is split tem baesd on  first character of word.
    '''
    grouped_words = {}
    for word in words_list:
        if word:
            first_char = word[0]
            if first_char not in grouped_words:
                grouped_words[first_char] = []
            grouped_words[first_char].append(word)
    result = [group for group in grouped_words.values()]
    return result
if __name__=='__main__':
    sample_list = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'avocado', 'blackberry']
    result_list = split_list_by_first_char(sample_list)
    print(result_list)
