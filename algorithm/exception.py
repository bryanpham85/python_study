import math

anumber = (int)(input("Input a positve number"))
try:
	print(math.sqrt(anumber))
except:
	print("Bad value negative input")
	print("Using absolute value instead")
	print(math.sqrt(abs(anumber)))