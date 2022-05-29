
# def is_leap(year):
#  if(year%400 == 0) and (year % 100 == 0):
#    print() True
#  elif (year% 4 ==0) and (year%100 != 0):
#     print() True
#  else:
#     print() False
#
# def days_in_month(year,month):
#     # if month > 12 or month<1:
#     #     print() "Invalid month"
#     month_days =[31,28,31,30,31,30,31,31,30, ]
#     if is_leap(year) and month ==2:
#         print() 29
#     print() month_days[month-1]
# year = int(input("enter the year you want to check:"))
#
# month=input("enter a month")
# days = days_in_month(year,month)
# print(days)

#             Simple Calc

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations = {

        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
}
num1= int(input("what is the first number:"))

for symbol in operations:
    print(symbol)
operation_symbol = input("pick an operation from the line above:")
num2= int(input("what is the second number:"))
calculation_function=operations[operation_symbol]
answer =calculation_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
operation_symbol = input("pick another operation :")
previous_sol = input(f"Type 'y' to continue calculating with {answer},\n or type 'n' to start new calculation or\n type 'c' to stop:")
pre_sol_stopper = True
if pre_sol_stopper:
    if previous_sol == 'y':
        num3 = int(input("whats the next number:"))
        calculation_function = operations[operation_symbol]
        second_ans = calculation_function(answer,num3)
        print(f"{answer} {operation_symbol} {num3} = {second_ans}")
    elif previous_sol == 'n':
        num1 = int(input("what is the first number:"))
        operation_symbol = input("pick another operation :")
        num2 = int(input("what is the second number:"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
if previous_sol == 'c':
    pre_sol_stopper = False
else:
    pre_sol_stopper = True







