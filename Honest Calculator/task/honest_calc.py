# write your code here
from typing import Union

msg = ["Enter an equation",
       "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
       "Yeah... division by zero. Smart move...",
       "Do you want to store the result? (y / n):",
       "Do you want to continue calculations? (y / n):",
       " ... lazy",
       " ... very lazy",
       " ... very, very lazy",
       "You are",
       "Are you sure? It is only one digit! (y / n)",
       "Don't be silly! It's just one number! Add to the memory? (y / n)",
       "Last chance! Do you really want to embarrass yourself? (y / n)"]

go: bool = False
memory: float = 0.
result: float = 0.


def read_equation():
    print(msg[0])
    calc = input()
    return calc.split()


def is_number(x_value: str) -> bool:
    try:
        float(x_value)
    except ValueError:
        return False
    else:
        return True


def check_xy(x_value: str, y_value: str) -> bool:
    """

    :rtype: bool
    """
    check_val: bool = (is_number(x_value) or x_value == 'M') and (is_number(y_value) or y_value == 'M')
    if not check_val:
        print(msg[1])
    return check_val


def check_operation(op_string: str) -> bool:
    """

    :rtype: bool
    """
    check_op: bool = op_string == '+' or op_string == '-' or op_string == '*' or op_string == '/'
    if not check_op:
        print(msg[2])
    return check_op


def calculate(x_value: float, op: str, y_value: float) -> Union[float, bool]:  # -> float | bool:
    error_code: bool = False
    if op == '+':
        return x_value + y_value
    if op == '-':
        return x_value - y_value
    if op == '*':
        return x_value * y_value
    if op == '/':
        try:
            return x_value / y_value
        except ZeroDivisionError:
            print(msg[3])
            return error_code


# def check_not_zero(y_value):
#     """ Probably superfluous now because of the try-except block """
#     if y_value == '0':
#         print(msg[3])
#     return y_value != '0'


def user_query(query_message: str) -> bool:
    # valid_response = False
    while True:  # not valid_response:
        print(query_message)
        response = input()
        if response == 'y':
            return True
        if response == 'n':
            return False


def is_one_digit(value: Union[int, float]) -> bool:
    """

    :type value: Union[int, float]
    """
    boundary = 10
    if value.is_integer() and -boundary < int(value) < boundary:
        return True
    else:
        return False


def check(x_value, op, y_value):
    opinion = ''
    if is_one_digit(x_value) and is_one_digit(y_value):
        opinion = opinion + msg[6]
    if (x_value == 1 or y_value == 1) and op == '*':
        opinion = opinion + msg[7]
    if (x_value == 0 or y_value == 0) and (op == '*' or op == '+' or op == '-'):
        opinion = opinion + msg[8]
    if opinion:
        print(msg[9] + opinion)


def assign_values(xv, yv):
    global memory

    if xv == 'M':
        xv = memory
    else:
        xv = float(xv)

    if yv == 'M':
        yv = memory
    else:
        yv = float(yv)
    return xv, yv


def honest_calc():
    global memory
    global go
    global result

    while True:
        x, operation, y = read_equation()

        go = check_xy(x, y) and check_operation(operation)
        if not go:
            continue
        else:
            x, y = assign_values(x, y)

        check(x, operation, y)

        result = calculate(x, operation, y)
        if type(result) == float:
            print(result)
        else:
            continue

        if user_query(msg[4]):
            store_result = True
            if is_one_digit(result):
                msg_index = 10
                while msg_index <= 12:
                    if user_query(msg[msg_index]):
                        msg_index += 1
                    else:
                        store_result = False
                        break

            if store_result:
                memory = result

        if not user_query(msg[5]):
            break


if __name__ == "__main__":
    honest_calc()
