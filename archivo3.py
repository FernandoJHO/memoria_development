# -*- coding: utf-8 -*-

 

# define la función

def mcd(a, b):

	resto = 0

	while(b > 0):

		resto = b

		b = a % b

		a = resto

	return a

num1 = int(input("Introduce el primer numero: \n"))

num2 = int(input("Introduce el segundo numero: \n"))

