problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(problems):

    limit = 5
    operators_allowed = ['+', '-']
    operators_disallowed = ['*', '/']
    
    if len(problems) > limit:
        raise ValueError('Error: Too many problems.')
