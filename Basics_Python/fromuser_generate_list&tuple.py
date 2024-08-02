'''
@Author: Manoj KR

@Date: 2024-07-27 14:40:30

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-27 15:00:10

@Title : which accepts a sequence of comma-separated numbers from user
         and generate a list and a tuple with those numbers.

'''



def generate(string):
     '''
    Description : which accepts a sequence of comma-separated numbers from user
                and generate a list and a tuple with those numbers.

    Parameter : 
              string(str) : numbers seperated by comma given by user.
     
    Return : 
           list(list) and tuple(tuple) : respective list and tuple which converts given string to list and tuple.

    '''
     list=string.split(",")
     return list,tuple(list)

def main():
    string=input("Enter the number seperated by comma(,) :")
    list,tuple=generate(string)
    print(list)
    print(tuple)
    
if __name__=="__main__":
   main()
   