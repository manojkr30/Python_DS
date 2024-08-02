'''
@Author: Manoj KR

@Date: 2024-07-27 14:03:00

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-27 14:20:30

@Title : Python program to print the calendar of a given month and year.

'''

import calendar

def print_month_calendar(year, month):
    """
    Description : to print the calendar of a given month and year.

    Parameter : 
              year (int) : year to find calander.
              month (int) : month to find calander.
     
    Return : None
    """
    # Create a TextCalendar instance
    cal = calendar.TextCalendar(calendar.MONDAY)
    # Print the month's calendar
    month_calendar = cal.formatmonth(year, month)
    print(month_calendar)

def main():
        year = int(input("Enter The Year ="))
        month = int(input("Enter The Month ="))
        print_month_calendar(year, month)
        
# main method
if __name__=="__main__":
    main()