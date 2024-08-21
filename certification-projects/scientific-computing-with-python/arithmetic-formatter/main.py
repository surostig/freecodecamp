# list problems to be formatted
# problems = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
# establish limits and operator conditions
prob_limit = 5
digit_limit = 4
operators_allowed = ['+', '-']
operators_disallowed = ['*', '/']
spacing = '    '

def errors(problems):
    if len(problems) > prob_limit:
        return 'Error: Too many problems.'
    
    is_number = lambda x : x.isnumeric()  
    
    for i in problems:

        components = i.split(' ')
        
        for i in components:

            # identify and assign operator
            if i in operators_allowed:
                operator = i

            # value error checks    
            elif i in operators_disallowed:

                return "Error: Operator must be '+' or '-'."
            
            if i not in operators_allowed+operators_disallowed and is_number(i) == False:

                return 'Error: Numbers must only contain digits.'
            
            if is_number(i) == True and len(i) > digit_limit:
                
                return 'Error: Numbers cannot be more than four digits.'

def _format(equation):
    elements = equation.split(' ')
    lenlist = []
    for element in elements:
        lenlist.append(len(element))
    padding = 2
    jlen = max(lenlist) + padding
    r1 = elements[0].rjust(jlen)
    r2 = elements[1] +' ' + elements[2].rjust(len(elements[0]))
    lines = ''
    for i in range(jlen):
        lines +=  '-'
    r3 = lines
    if elements[1] == "+":
        answer = int(elements[0]) + int(elements[2]) 
    elif elements[1] == "-":
        answer = int(elements[0]) - int(elements[2])
    r4 = str(answer).rjust(jlen)
    return [r1+spacing, r2+spacing, r3+spacing, r4+spacing]

def arithmetic_arranger(problems, showans = False):
    if errors(problems):
        return errors(problems)
    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''
    formattedequations = []
    for problem in problems:
           formattedequations.append(_format(problem))
    for i in range(len(problems)):
        r1 += formattedequations[i][0]
        r2 += formattedequations[i][1]
        r3 += formattedequations[i][2]
        r4 += formattedequations[i][3]
    if showans == False:
        output = r1.rstrip()+'\n'+r2.rstrip()+'\n'+r3.rstrip()
        return output
    elif showans == True:
        output = r1.rstrip()+'\n'+r2.rstrip()+'\n'+r3.rstrip()+'\n'+ r4.rstrip()
        return output
    return print(output)

arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
