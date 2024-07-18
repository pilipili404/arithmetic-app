# arithmetic_app/arithmetic.py
def arithmetic_arranger(problems, show_answers=False):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    logging.debug(f"Received problems: {problems}")

    if len(problems) > 5:
        return "Error: Too many problems."

    operators = []
    numbers = []

    for problem in problems:
        array = problem.split()
        logging.debug(f"Splitting problem '{problem}' into: {array}")

        if len(array) != 3:
            logging.error(f"Problem '{problem}' is not formatted correctly.")
            return f"Error: Problem '{problem}' is not formatted correctly."

        operators.append(array[1])
        numbers.append(array[0])
        numbers.append(array[2])

    for operator in operators:
        if operator not in ['+', '-']:
            logging.error(f"Operator '{operator}' is not valid.")
            return "Error: Operator must be '+' or '-'."

    for number in numbers:
        if not number.isdigit():
            logging.error(f"Number '{number}' contains non-digits.")
            return "Error: Numbers must only contain digits."
        elif len(number) > 4:
            logging.error(f"Number '{number}' is too long.")
            return "Error: Numbers cannot be more than four digits."

    answers = []
    top_row = ''
    bottom_row = ''
    answer_row = ''
    dashes = ''

    for i in range(0, len(numbers), 2):
        num1 = int(numbers[i])
        num2 = int(numbers[i + 1])
        operator = operators[i // 2]

        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2
        answers.append(result)

        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        top_row += numbers[i].rjust(space_width)
        bottom_row += operator + numbers[i + 1].rjust(space_width - 1)
        dashes += '-' * space_width

        if i != len(numbers) - 2:
            top_row += ' ' * 4
            bottom_row += ' ' * 4
            dashes += ' ' * 4

    for i in range(len(answers)):
        space_width = max(len(numbers[2 * i]), len(numbers[2 * i + 1])) + 2
        answer_row += str(answers[i]).rjust(space_width)

        if i != len(answers) - 1:
            answer_row += ' ' * 4

    if show_answers:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, answer_row))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))

    return arranged_problems

