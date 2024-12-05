import calculator_art
print(calculator_art.calculator_ascii)
def add(number1, number2):
    return number1 + number2
def substract(number1, number2):
    return number1 - number2
def multiply(number1, number2):
    return number1 * number2
def divide(number1, number2):
    return number1 / number2

calculator_operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

number1 = float(input("Enter the firs number: "))
for symbol in calculator_operations:
    print(symbol)
operation_symbol = input("Which operations? ")
number2 = float(input("Enter the second number"))

answer = calculator_operations[operation_symbol](number1, number2)

print(answer)

