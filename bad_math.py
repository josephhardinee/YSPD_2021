import numpy as np

def pow(x:float, power:float):
	return x**2

def a_unnecessarily_long_function(x:int, y:float):
	""" Of course we put a comment string in our function explaining what it does right?
	"""

	if x < 0:
		t=y*x
	if x> 0:
		t=y*-1*x

	if t>0:
		return 0
	else:
		return 1


