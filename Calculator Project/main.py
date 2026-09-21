from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}


def calculate(operation, n1, n2):
    result = operations[operation](n1, n2)
    return result
keep_going = True

num1 = float(input("What is your first number?: "))
for key in operations:
    print(key)




while keep_going == True:
    oper = input('Choose an operation "+", "-", "*" or "/": ')
    num2 = float(input("What is your next number?: "))
    result = calculate(oper, num1, num2)
    print(result)

    another_calc = input("want to keep doing math? y/n: ")
    if another_calc == 'y':
        num1 = result


    elif another_calc == 'n':
        print("\n" * 20)
        keep_going == False
        break