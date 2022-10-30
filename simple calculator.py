# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:49:57 2022

@author: Asus
"""

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

operator = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}

number1 = float(input('Enter the first number: '))

should_continue = False
while not should_continue:
    for keys in operator:
        print (keys)
    operation = input('Select operation: ')

    number2 = float(input('Enter another number: '))
    calculate = operator[operation]
    c1 = calculate(number1,number2)
    print(f"{number1} {operation} {number2} = {c1}")

    con = input(f"do you want to continue the calculation with the answer {c1}? write 'yes' or 'no'")

    if con == 'no':
        should_continue = True
    else:
        number1 = c1