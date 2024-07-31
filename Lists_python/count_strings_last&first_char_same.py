''''
@Author: Manoj KR

@Date: 2024-07-29 11:20:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 11:35:11

@Titl:Python program to count the number of strings where the string length
      is 2 or more and the first and last character are same from a given list of strings.
'''
def count_of_string(list_items):
    ''''
    Description : To count the number of strings where the string length is 2 or more and the
                  first and last character are same from a given list of strings.

    Parameter : 
              list_items : list having string items .
    Return : 
            count : count of strings where the string length is 2 or more and the first and last character are same.
    '''
    count=0
    for item in list_items:
        if len(item) >= 2 and item[0]==item[len(item)-1] :
            count +=1
    return count
     

def main():
    list_items=['abc', 'xyz', 'aba', '1221']
    print("count of strings where the string length is 2 or more and the first and last character are same from a given list are ")
    print(count_of_string(list_items))
 
if __name__=="__main__":
    main()