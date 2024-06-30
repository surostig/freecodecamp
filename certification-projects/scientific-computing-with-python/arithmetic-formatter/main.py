problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(problems):

    limit = 5
    operators_allowed = ['+', '-']
    operators_disallowed = ['*', '/']
    
    if len(problems) > limit:
        raise ValueError('Error: Too many problems.')

    for problem in problems:
        pass

def main():
    return arithmetic_arranger(problems)

main()

test = problems[1].split(' ')
print(f'The first problem is {test}')
for i in test:
    print (i.isnumeric(), i.isalpha())
