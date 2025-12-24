select = input("trying to find what side? a , b or hypotenuse {all of a right angle triangle}")
import math

def trig_a(b,c):
	a = math.sqrt( c**2 - b**2)
	return a
def trig_b(a,c):
	b = math.sqrt(c**2 - a**2)
	return b
def trig_c(a,b):
	c = math.sqrt(a**2 + b**2) 
	return c 
if select == "a":
	b = float(input("b = "))
	c = float(input("c = "))
	print(f"a= {trig_a(b,c)}")
elif select == "b": 
	a = float(input("a = ")) 
	c = float(input("c = ")) 
	print(f"b = {trig_b(a,c)}")
elif select == "c": 
	a = float(input("a = ")) 
	b = float(input("b = ")) 
	print(f"c = {trig_c(a,b)}") 
else: 
	print("invalid input , input must be a,b or c where letter corresponds to missing length") 
