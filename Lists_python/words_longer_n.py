''''
@Author: Manoj KR

@Date: 2024-07-29 12:44:09

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 12:54:39

@Titl: Python program to find the list of words that are longer than n from a
       given list of words.
'''

def words_longer_then(words,n):
   ''''
    Description : To return the list of words that are longer than n given by user.

    Parameter : 
              words: containg words of list.
    Return : 
             return the list that having words that longer then the n.
    '''
   return [word for word in words if len(word)>n]

def main():
   words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
   n=int(input("enter the lenth n="))
   print(words_longer_then(words,n))

if __name__=="__main__":
   main()