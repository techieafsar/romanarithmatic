
def operator_sel(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        return num1 // num2
    elif operator == '*':
        return num1 * num2
    else:
        raise ValueError("inappropriate operator selected")