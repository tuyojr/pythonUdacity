def arithmetic_arranger(problems, result=False):
    # Checks If there are more than 5 problems supplied to the function.
    if len(problems) > 5:
        return "Error: Too many problems."

    # Define the arithmetic operators with a lambda function and store them in a dictionary
    operators = {
        '+': lambda num: str(num[0] + num[1]),
        '-': lambda num: str(num[0] - num[1])
    }

    # Create an empty list to hold the values passed in, in an arranged manner
    arranged_problems = []

    # An empty list to hold the values in an arranged manner
    first = []
    second = []
    lines = []
    results = []

    # Loop through each arithmetic problem passed into the function
    for problem in problems:

        # Split them into individual problems
        chunks = problem.split()

        # check the length of the problem, using the maximum length of the chunks str as the value
        max_len = len(max(chunks, key=len))

        # for error handling, check if all the items in the problem are numeric values only at index 0, skipping index 1, to index 2
        if not all([i.isnumeric() for i in chunks[::2]]):
            return "Error: Numbers must only contain digits."

        # check if the element of the problem at index 1 is not an operator key in the operator dictionary above  
        elif chunks[1] not in operators.keys():
            return "Error: Operator must be '+' or '-'."

        # check if each element is more than 4
        elif max_len > 4:
            return "Error: Numbers cannot be more than four digits."

        # the line_len creates the length of each line. we add the length of the problem to 2 which represents the sign and the space, we then store the dotted line '-' in a line variable and multiply it by how many times it should be reproduced
        line_len = max_len + 2
        line = '-' * line_len  

        # this sets the first number justified to the right and puts a single space after it
        first_num = chunks[0].rjust(line_len, ' ')

        # formatting the second line, where we set the operator (chunks[1]), give some space (which is multiplied by the line length and subtracted from the length of the second number minus 1 to get an accurate amount of space), and then the value of the second number
        second_num = f"{chunks[1]}{' ' * (line_len - len(chunks[2]) - 1)}{chunks[2]}"

        # here we add the values to our list created above
        first.append(first_num)
        second.append(second_num)
        lines.append(line)

        # we set the value of the result by creating a res variable which uses the operator on the two numbers converted to integers
        if result:
            res = operators[chunks[1]]([int(i) for i in chunks[::2]])

            # we add the value of the result in the manner we want, same as we did for both numbers above
            results.append(f"{res.rjust(line_len, ' ')}")

    # we join the values of the 1st, 2nd numbers and the dashed lines to the final arranged problems
    arranged_problems = '\n'.join(['    '.join(i)
                                   for i in (first, second, lines)])

    # we join the results for the final arranged problems here
    if results:
        arranged_problems += '\n' + '    '.join(results)

    # return the value of the arranged problems
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))