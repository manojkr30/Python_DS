'''
@Author: Manoj KR

@Date: 2024-07-27 16:62:10

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-27 17:15:18

@Title : To print out a set containing all the colors from color_list_1 which
         are not present in color_list_2.
'''

def remove_color(color_list1,color_list2):
    """
    Description : To print out a set containing all the colors from color_list_1 which
                  are not present in color_list_2.
    Parameter : 
              color_list1,color_list2:list having colors
     
    Return : list which color_list1  colors not in  color_list2
    """
    return color_list1-color_list2

if __name__=="__main__":
    color_list1 = set(["White", "Black", "Red"])
    color_list2 = set(["Red", "Green"])
    print(remove_color(color_list1,color_list2))