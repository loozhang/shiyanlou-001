#!/usr/bin/env python3
import sys
try:
	salary=int(sys.argv[1])
	num1=salary-3500
	if num1<=0:
        	print(format(0,".2f"))
	elif num1<=1500:
        	print(format(num1*0.03,".2f"))
	elif num1<=4500:
        	print(format(num1*0.1-105,".2f"))
	elif num1<=9000:
        	print(format(num1*0.2-555,".2f"))
	elif num1<=35000:
        	print(format(num1*0.25-1005,".2f"))
	elif num1<=55000:
        	print(format(num1*0.3-2755,".2f"))
	elif num1<=80000:
        	print(format(num1*0.35-5505,".2f"))
	elif num1>80000:
        	print(format(num1*0.45-13505,".2f"))
except:
        print("Parameter Error")

