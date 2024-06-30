problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(problems):

    limit = 5
    operators_allowed = ['+', '-']
    operators_disallowed = ['*', '/']
    
    def operator_check(operator):
        if operator in operators_allowed:
            pass
        elif operator in operators_disallowed:
            raise ValueError("Error: Error: Operator must be '+' or '-'.")
    
    if len(problems) > limit:
        raise ValueError('Error: Too many problems.')

    for problem in problems:
        pass

def main():
    return arithmetic_arranger(problems)

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
    print(tests)
