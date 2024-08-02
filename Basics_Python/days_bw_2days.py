'''
@Author: Manoj KR

@Date: 2024-07-27 16:03:00

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-27 16:20:30

@Title : program to calculate number of days between two dates.

'''

from datetime import date

def days_between_dates(date1, date2):
    """
    Description : to calculate number of days between two dates given by user.

    Parameter : 
              date1 (int) : first date.
              date2 (int) : second date.
     
    Return : number of days between two dates date2 - date1 .
    """
    # Convert the tuples to date objects
    d1 = date(*date1)
    d2 = date(*date2)
    # Calculate the difference
    delta = d2 - d1
    return delta.days

days_between_dates((2014/7/1),(2014/7/10))