def format_problem(operator, number1, number2):
  if operator == '+':
    total = str(int(number1) + int(number2))
  else:
    total = str(int(number1) - int(number2))
  problem_width = max(len(number1), len(number2)) + 2
  line1 = number1.rjust(problem_width)
  line2 = operator + number2.rjust(problem_width - 1)
  line3 = problem_width * '-'
  line4 = total.rjust(problem_width)
  return [line1, line2, line3, line4]

def arithmetic_arranger(problems, include_solution=False):  
  if len(problems) > 5:
    return 'Error: Too many problems.'
  else:
    solution_matrix = [[],[],[],[]]
    for problem in problems:
      number1, operator, number2 = problem.split()
      try:
        int(number1) and int(number2)
      except: 
        return 'Error: Numbers must only contain digits.'
      if operator == '/' or operator == '*':
        return 'Error: Operator must be \'+\' or \'-\'.'
      elif len(number1) > 4 or len(number2) > 4:
        return 'Error: Numbers cannot be more than four digits.'
      else:
        formatted_problem = format_problem(operator, number1, number2)
        i = 0
        while i <= 3:
          solution_matrix[i].append(formatted_problem[i])
          i += 1
    solution = ''
    end = 3 if include_solution else 2
    i = 0
    while i <= end:
      solution += '    '.join(solution_matrix[i]) + '\n'
      i += 1
    return solution[:-1]
