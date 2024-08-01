'''
@Author: Manoj KR

@Date: 2024-07-25 15:46:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 15:54:18

@Title : program to  generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
'''
def generate(n):
    '''
     Description : to generate  dictionary that contains a number (between 1 and n) in the form (x, x*x).

    Parameter : 
              n :the user given n integer value where dictionary have element from 1 to n.
     
    Return : 
           dict : having n element given by the user  from 1 to n in  the form (x, x*x).
    '''
    dict={}
    for i in range(1,n+1):
        dict.update({i : i*i})
    return dict

if __name__=='__main__':
    n=int(input("Enter the number of element you want in dictinary :"))
    print(generate(n))