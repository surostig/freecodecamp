# list problems to be formatted
problems = ["32 + 698", "301 - 2", "45 + 43", "123 + 49"]

# establish limits and operators allowed/disallowed

def arithmetic_arranger(problems, show_answer=False):
    problems_limit = 5
    digit_limit = 4
    operators_allowed = ['+', '-']
    operators_disallowed = ['*', '/']
    is_number = lambda x : x.isnumeric()  

    for i in problems:

        components = i.split(' ')

        for i in components:
            print(i, is_number(i))
            # identify and assign operator
            if i in operators_allowed:
                operator = i

            # value error checks    
            elif i in operators_disallowed:

                raise ValueError("Error: Operator must be '+' or '-'.")
            
            if i not in operators_allowed+operators_disallowed and is_number(i) == False:

                raise ValueError('Error: Numbers must not contain letters')
            
            if len(i) > digit_limit:
                
                raise ValueError('Error: Numbers cannot be more than four digits.')
     
arithmetic_arranger(problems)
