#!/usr/bin/env python
#----------------------------------------------------------------------
# Name of file: make_math_page.py
# Author: Karl Fritz
# Date: October 11, 2015
# Description: This program takes the following input from a user:
#              - Two numbers (which the program used to determine the
#                  maximum and minimum numbers to be used in the math
#                  problems)
#              - The type of operation
#              - the program then creates two files:
#                  "math_answers.txt" - a file with the problems and 
#                  answers
#                  "math_problems.txt" - a file with only the problems
#                  (this is the one you give to your child)
#              This program was written to help my daughter increase
#              her performance with respect to solving a number of
#              math problems in a given time period 
#              (e.g. "How many math probs can be solved in 5 minutes")
#
# Usage: python make_math_page.py
# Python version: Python 2.7
#
# The author makes no guarantees about this software and is not
# reponsible for any adverse results from execution
#
# Change log:
# 10/11/2015   Initial release
# 10/11/2015   Added nofication message that worksheet files have been generated
# 10/11/2015   Now adds a date to the filename, also increased maximum number of problems
#              to 100 per page

from __future__ import print_function
import random
import sys
import fileinput
import time

def int_raw_input(prompt):
    while True:
        try:
            # if the call to int() raises an
            # exception, this won't return here
            return int(raw_input(prompt))
        except ValueError:
            # simply ignore the error and retry
            # the loop body (i.e. prompt again)
            pass

def user_problem_type_select():
    while True:
        try:
            prob_type = int(raw_input("Enter problem type (1)add, (2)sub, (3)mult: "))
            if 1 <= prob_type < 4:       
                return prob_type
            else:
                    print("Invalid entry, please select 1, 2, or 3")  
        except ValueError:
            # simply ignore the error and retry
            # the loop body (i.e. prompt again)
            pass      


def random_nums(x, y): 
    a = random.randint(min(x, y), max(x, y))
    b = random.randint(min(x, y), max(x, y)) 
    if a > b:
        return {'a':b, 'b':a} 
    else:
        return {'a':a, 'b':b} 


def problems(number_per_row, prob_type):
    values = []
    a = []
    b = []
    result = []
    for i in range(number_per_row):
        values.append(random_nums(x, y))

    for j in range(number_per_row):
        b.append(str(values[j]['b']))
        a.append(str(values[j]['a']))

        if prob_type == 1:
            result.append(str(values[j]['b'] + values[j]['a']))

        elif prob_type == 2:
            result.append(str(values[j]['b'] - values[j]['a']))

        else:
            result.append(str(values[j]['b'] * values[j]['a']))

    return {'b':b, 'a':a, 'result':result}


def problem_sheet(row_probs, rows, prob_type):
    for math_rows in range(rows):
        math_probs = []
        math_probs.append(problems(row_probs, prob_type))

        row_b = ""
        row_a = ""
        row_m = ""
        row_r = ""
        row_s = ""

        for prob in range(row_probs):
            width = max(len(str(math_probs[0]['a'][prob])),len(str(math_probs[0]['b'][prob])))  # used for justification purposes
            row_b += " " + str(math_probs[0]['b'][prob]).rjust(width) + "    "

            if prob_type == 1:
                row_a += "+" + str(math_probs[0]['a'][prob]).rjust(width) + "    "
            elif prob_type == 2:
                row_a += "-" + str(math_probs[0]['a'][prob]).rjust(width) + "    "
            else:
                row_a += "x" + str(math_probs[0]['a'][prob]).rjust(width) + "    "

            row_m += " " + "-" * max(len(str(math_probs[0]['a'][prob])),len(str(math_probs[0]['b'][prob]))) + "    "
            row_r += " " + str(math_probs[0]['result'][prob]).rjust(width) + "    "
            row_s += ""
            row_s += ""

        # put problems in the file (no answers though)
        print(row_b, file = mp)
        print(row_a, file = mp)
        print(row_m, file = mp)
        print(row_s, file = mp)
        if math_rows < rows - 1:  # only print a line of spaces if its not the last row
            print(row_s, file = mp)

        # put problems and answers in the other file
        print(row_b, file = ma)
        print(row_a, file = ma)
        print(row_m, file = ma)
        print(row_r, file = ma)
        if math_rows < rows - 1:  # only print a line of spaces if its not the last row
            print(row_s, file = ma)


if __name__ == "__main__":
    x = int_raw_input("Enter a number: ")
    y = int_raw_input("Enter another number: ")
    prob_type = user_problem_type_select()
    today_date = time.strftime("%m%d%Y")


    # calculate the number of problems in a row based on how large the numbers are
    row_probs = int(70 / (int(max(len(str(x)),len(str(y)))) + 5))
    rows = 10

    # Open a plain text files for putting math problems and answers into
    mp = open("math_problems_%s.txt"%today_date, "w+")
    ma = open("math_answers_%s.txt"%today_date, "w+")

    # call function to generate math problems
    problem_sheet(row_probs, rows, prob_type)

    print("Files %s and %s have been generated"%(mp.name, ma.name))
