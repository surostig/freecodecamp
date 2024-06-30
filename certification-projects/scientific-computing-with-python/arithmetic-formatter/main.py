# list problems to be formatted
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
operators_allowed = ['+', '-']
operators_disallowed = ['*', '/']

# create arranger function for the problems
def arithmetic_arranger(problems):

# establish limits and operators allowed/disallowed
    limit = 5
    
# check whether operator is allowed or disallowed
    def operator_check(operator):
        if operator in operators_allowed:
            pass
        elif operator in operators_disallowed:
            raise ValueError("Error: Error: Operator must be '+' or '-'.")

# check if problem list is within limit    
    if len(problems) > limit:
        raise ValueError('Error: Too many problems.')

# proceed to arrange problems if list within limit


def main():
    return arithmetic_arranger(problems)

# run the arranger
main()

# select a test problem to analyze
test = problems[0].split(' ')
print(f'The first problem is {test}')   

# analyze strings in test
for string in test:
    tests = []
    tests.append(type(string))
    tests.append(len(string))
    tests.append(string)
    if string in operators_allowed + operators_disallowed:
       print(f'The operator is {string}') 


