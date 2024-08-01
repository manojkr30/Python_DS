'''
@Author: Manoj KR

@Date: 2024-07-25 15:31:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-25 15:39:18

@Title : to concatenate following dictionaries to create a new one.
'''
def concatinate(dict1,dict2,dict3):
    """
    Description : to concatenate following 3 dictionaries to create a new one.

    Parameter : 
              dict1 ,dict2 ,dict3 :the 3 dictionaries to be add in one dictionary.
     
    Return :
            dict4 : the concatinated one having all 3 key and values.
    """
    dict4={}
    dict4.update(dict1)
    dict4.update(dict2)
    dict4.update(dict3)
    return dict4

if __name__=='__main__':
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    result_dict=concatinate(dic1,dic2,dic3)
    print(result_dict)
