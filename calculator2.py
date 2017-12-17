#!/usr/bin/env python3
import sys
def calculate_tax(before_tax):
    if before_tax<=0:
        tax=0
    elif before_tax<=1500:
        tax=before_tax*0.03
    elif before_tax<=4500:
        tax=before_tax*0.1-105
    elif before_tax<=9000:
        tax=before_tax*0.2-555
    elif before_tax<=35000:
        tax=before_tax*0.25-1005
    elif before_tax<=55000:
        tax=before_tax*0.3-2755
    elif before_tax<=80000:
        tax=before_tax*0.35-5505
    elif before_tax>80000:
        tax=before_tax*0.45-13505
def calculate_salary(salary):
    before_tax=salary-salary*0.165-3500
    tax=calculate_tax(before_tax)
    real_salary=salary-tax-salary*0.165
    return real_salary
args=[]
for arg in sys.argv[1:]:
    args.append(arg)
scores={}
for arg in args:
    list1=arg.split(':')
    try:
        real_salary=calculate_salary(int(list1[1]))
    except:
        print("Parameter Error")
    print(list1[0]+':'+format(real_salary,"0.2f"))
