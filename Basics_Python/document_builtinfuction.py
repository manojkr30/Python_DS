'''
@Author: Manoj KR

@Date: 2024-07-27 16:03:00

@Last Modified by: Manoj KR

@Last Modified time: 2024-07-27 16:20:30

@Title : To print the documents (syntax, description etc.) of Python built-in function(s).
'''

def print_builtin_doc(function_name):
    '''
    Description : To print the documents (syntax, description etc.) of Python built-in
                  function(s).
    Parameter : 
              function_name(str) : fuction name to print the documents.
    '''
    try:
        # Get the built-in function object
        func = getattr(__builtins__, function_name)
        # Print the documentation header
        print(f"Function: {function_name}")
        # Print the function's docstring
        print(func.__doc__)
    except AttributeError:
        print(f"No built-in function named '{function_name}' found.")


def main():
    print_builtin_doc('abs')

if __name__=="__main__":
    main()